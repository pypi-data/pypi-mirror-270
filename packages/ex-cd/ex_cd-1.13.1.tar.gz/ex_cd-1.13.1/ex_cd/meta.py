import os
import re
import json
import ex_cd.gallery_dl_exec as gallery_dl
from .common import META_FOLDER, metadata_args, _get_gallery_metadata_files_path, get_gallery_one_metadata


def _download_gallery_meta(url, gallery_dir, config, logger):
    """download gallery metadata by gallery_dl"""
    if _valid_gallery_meta(url, gallery_dir, config, logger):  # validate the gallery
        return  # exit
    gallery_dl_exec = config["gallery-dl-exec"]
    gallery_dl_meta_args = config["gallery-dl-meta-args"]
    args = [*gallery_dl_exec, "--no-download", *metadata_args, *gallery_dl_meta_args, url]
    logger.debug(f"Exec: {args}")
    returncode = gallery_dl.main(*args)
    if _valid_gallery_meta(url, gallery_dir, config, logger):  # validate the gallery
        return  # record that this gallery has been downloaded
    elif returncode != 0:
        raise RuntimeError(f"Download gallery meta failed: {url} -> {gallery_dir}")
    else:
        raise RuntimeError(f"Download gallery meta invalid: {url} -> {gallery_dir}")


url2gid_re = re.compile(r"^https://e[-x]hentai.org/g/([0-9]+)/[0-9a-z]+/*$")


def _url2gid_by_re(url):
    return re.findall(url2gid_re, url)[0]


url2site_re = re.compile(r"(^https://e[-x]hentai.org)/g/[0-9]+/[0-9a-z]+/*$")


def _url2site_by_re(url):
    return re.findall(url2site_re, url)[0]


META_DOWNLOAD_RESUME_FILE = 'MetaDownloadResume'
META_VALIDATE_COMPLETED_FILE = 'MetaValidateCompleted'


def _valid_gallery_meta(url, gallery_dir, config, logger):
    """validate the gallery metadata"""
    ok_file = os.path.join(gallery_dir, META_FOLDER, META_VALIDATE_COMPLETED_FILE)
    if os.path.isfile(ok_file):  # if valid
        return True  # exit
    # check if has enough metadata json files
    meta = get_gallery_one_metadata(url, gallery_dir, config, logger)
    if 'filecount' not in meta:
        logger.error(f"Invalid {gallery_dir}: 'filecount' not in metadata")
        return False
    image_tokens = [None] * int(meta['filecount'])
    site, gid = _url2site_by_re(url), _url2gid_by_re(url)
    for metafile in _get_gallery_metadata_files_path(gallery_dir):
        try:
            with open(metafile, "r", encoding="utf8") as fp:
                meta = json.load(fp)
                if str(meta["gid"]) == gid:
                    image_tokens[meta["num"] - 1] = meta["image_token"]
        except Exception as e:
            logger.error(f"Invalid metadata {metafile}: {e}")
    resume_url = url
    for i, image_token in enumerate(image_tokens):
        if image_token:
            resume_url = f"{site}/s/{image_token}/{gid}-{i+1}"
        else:
            break
    if None in image_tokens:
        resume_file = os.path.join(gallery_dir, META_FOLDER, META_DOWNLOAD_RESUME_FILE)
        with open(resume_file, "w", encoding='utf8') as fp:
            fp.write(resume_url)
            logger.error(f"Invalid {gallery_dir}: no enough metadata files, should resume from {resume_url}")
            return False

    with open(ok_file, "w", encoding='utf8'):
        return True  # record that this gallery has been validated
