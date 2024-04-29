# Auto-generated test for dwi2mask_consensus

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwi2mask_consensus


def test_dwi2mask_consensus(tmp_path, cli_parse_only):

    task = dwi2mask_consensus(
        in_file=File.sample(),
        out_file=File.sample(),
        algorithms=File.sample(),
        masks=File.sample(),
        template=File.sample(),
        threshold=1.0,
        grad=File.sample(),
        fslgrad=File.sample(),
        nocleanup=True,
        scratch=File.sample(),
        cont=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
