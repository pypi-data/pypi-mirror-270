# Auto-generated test for dwinormalise_manual

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwinormalise_manual


def test_dwinormalise_manual(tmp_path, cli_parse_only):

    task = dwinormalise_manual(
        input_dwi=File.sample(),
        input_mask=File.sample(),
        output_dwi=File.sample(),
        grad=File.sample(),
        fslgrad=File.sample(),
        nocleanup=True,
        scratch=File.sample(),
        cont=File.sample(),
        debug=True,
        force=True,
        intensity=1.0,
        percentile=1,
    )
    result = task(plugin="serial")
    assert not result.errored
