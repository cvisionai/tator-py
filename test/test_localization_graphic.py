import datetime
import random
import uuid
import time

from PIL import Image
import numpy as np

import tator

def _ints_almost_equal(
    a: int,
    b: int,
    tolerance=1) -> bool:
    """ Returns true if the integers are almost equal (applying tolerance)

    Args:
        a, b: integers to compare (e.g. pixel)
        tolerance: integer tolerance to add for almost equal

    Returns:
        True if almost equal within the provided tolerance. False otherwise.

    """

    return abs(a - b) <= tolerance

def _random_localization(
    project: int,
    media_id: int,
    dtype: str,
    type_id: int,
    frame: int) -> dict:
    ''' Creates a dicctionary defining a randomized localization based on given parameters

    Args:
        project: Unique project ID
        media_id: Unique media ID
        dtype: 'box' or 'dot' or 'line'
        type_id: Unique ID associated with the given localization type
        frame: Frame number associated with the localization

    Returns:
        Dictionary version of the localization object

    '''

    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)

    if dtype == 'box':
        width = random.uniform(0.0, 1.0 - x)
        height = random.uniform(0.0, 1.0 - y)
        u = 0.0
        v = 0.0

    elif dtype == 'line':
        width = 0.0
        height = 0.0
        u = random.uniform(0.0, 1.0)
        v = random.uniform(0.0, 1.0)

    elif dtype == 'dot':
        width = 0.0
        height = 0.0
        u = 0.0
        v = 0.0

    else:
        raise ValueError("Invalid dtype provided")

    datum = {
        'x': x,
        'y': y,
        'width': width,
        'height': height,
        'u': u,
        'v': v,
        'project': project,
        'media_id': media_id,
        'type': type_id,
        'frame': frame,
    }

    attributes = {
        'test_bool': random.choice([False, True]),
        'test_int': random.randint(-1000, 1000),
        'test_float': random.uniform(-1000.0, 1000.0),
        'test_enum': random.choice(['a', 'b', 'c']),
        'test_string': str(uuid.uuid1()),
        'test_datetime': datetime.datetime.now().isoformat(),
        'test_geopos': [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        'test_float_array': [random.uniform(-1.0, 1.0) for _ in range(3)],
    }

    datum = {**datum, **attributes}

    return datum

def _generate_truth_info(
        localization_datum: dict,
        media_width: int,
        media_height: int,
        dtype: str,
        margins: tuple=None) -> tuple:
    """ Returns dictionary of truth information used for unit test comparisons

    Args:
        localization_datum: Dictionary schema defining a localization
        media_width: Width of media in pixels
        media_heieght: Height of media in pixels
        dtype: 'box', 'line', or 'dot' defining the localization types
        margins: Tuple where [0] is width (pixels), [1] is height(pixels). If none, then ignored.

    Returns:
        Tuple where [0] is width (pixels), [1] is height (pixels)
    """

    MINIMUM_PIXEL_SIZE = 3

    # Define the truth widths and heights (without margins) in pixel space
    if dtype == 'box':
        truth_width = localization_datum['width'] * media_width
        truth_height = localization_datum['height'] * media_height
        default_margins = (0, 0)

    elif dtype == 'line':
        point_a = (localization_datum['x'], localization_datum['y'])
        point_b = (point_a[0] + localization_datum['u'], point_a[1] + localization_datum['v'])
        truth_width = abs(point_a[0] - point_b[0]) * media_width
        truth_height = abs(point_a[1] - point_b[1]) * media_height
        default_margins = (10, 10)

    else: # Dot
        truth_width = 1
        truth_height = 1
        default_margins = (10, 10)

    # Apply specific margins if provided. Otherwise use default.
    if margins is not None:
        truth_width += margins[0] * 2
        truth_height += margins[1] * 2

    else:
        truth_width += default_margins[0] * 2
        truth_height += default_margins[1] * 2

    # Constrain to media size and expected minimum size
    if truth_width > media_width:
        truth_width = media_width
    elif truth_width <= MINIMUM_PIXEL_SIZE:
        truth_width = MINIMUM_PIXEL_SIZE

    if truth_height > media_height:
        truth_height = media_height
    elif truth_height <= MINIMUM_PIXEL_SIZE:
        truth_height = MINIMUM_PIXEL_SIZE

    return round(truth_width), round(truth_height)

def _perform_specific_box_size_test(
        host: str,
        token: str,
        project: int,
        media_id: int,
        box_type: int,
        x: float,
        y: float,
        width: int,
        height: int,
        margins: tuple=None) -> None:
    """ Performs testing with the given parameters using a specific localization box size

    Single test performed. It's based on figuring out the truth width/height and requesting
    the graphic associated with the localization. The truth width/height is then
    compared against the image returned.

    There is a tolerance applied due to floating point rounding going from
    relative to absolute dimensions.

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
        media_id: Unique identifier of media associated with the localization
        box_type: Unique identifier of the test box localization type
        x: X value of the box localization (relative)
        y: Y value of the box localization (relative)
        width: Width of the box localization (pixels)
        height: Height of the box localization (pixels)
        margins: Width/height of the margins to apply (pixels). None if should be ignored.
    """

    # Create interface
    tator_api = tator.get_api(host, token)
    media = tator_api.get_media(media_id)

    # Create the localizations and send it over to the server
    if media.num_frames is not None:
        FRAME_NUMBER = random.randint(0, media.num_frames - 1)
    else:
        FRAME_NUMBER = 0

    # Create localization
    datum = {
        'x': x,
        'y': y,
        'width': width / media.width,
        'height': height / media.width,
        'u': 0.0,
        'v': 0.0,
        'project': project,
        'media_id': media_id,
        'type': box_type,
        'frame': FRAME_NUMBER,
    }

    attributes = {
        'test_bool': random.choice([False, True]),
        'test_int': random.randint(-1000, 1000),
        'test_float': random.uniform(-1000.0, 1000.0),
        'test_enum': random.choice(['a', 'b', 'c']),
        'test_string': str(uuid.uuid1()),
        'test_datetime': datetime.datetime.now().isoformat(),
        'test_geopos': [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        'test_float_array': [random.uniform(-1.0, 1.0) for _ in range(3)],
    }

    datum = {**datum, 'attributes': {**attributes}}
    response = tator_api.create_localization_list(project, body=datum)

    # Generate the truth information for unit testing
    truth_graphic_info = {}
    for localization_id in response.id:
        truth_graphic_info[localization_id] = _generate_truth_info(
            localization_datum=datum,
            media_width=media.width,
            media_height=media.height,
            dtype='box',
            margins=margins)

    # Cycle through the localizations, create the thumbnail and compare the image sizes
    for localization_id in truth_graphic_info:

        truth_width = truth_graphic_info[localization_id][0]
        truth_height = truth_graphic_info[localization_id][1]

        if margins is None:
            image_path = tator_api.get_localization_graphic(localization_id)
        else:
            image_path = tator_api.get_localization_graphic(
                localization_id,
                use_default_margins=False,
                margin_x=margins[0],
                margin_y=margins[1])

        img = Image.open(image_path)
        assert _ints_almost_equal(img.size[0], truth_width)
        assert _ints_almost_equal(img.size[1], truth_height)

def _perform_random_sizes_test(
        host: str,
        token: str,
        project: int,
        media_id: int,
        dot_type: int,
        line_type: int,
        box_type: int,
        margins: tuple=None,
        image_size: tuple=None) -> None:
    """ Performs testing with localizations of different types/sizes

    Tests are based on figuring out the truth width/height and requesting
    the graphic associated with each localization. The truth width/height is then
    compared against the image returned.

    There is a tolerance applied due to floating point rounding going from
    relative to absolute dimensions.

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
        media_id: Unique identifier of media associated with the localization
        dot_type: Unique identifier of the test dot localization type
        line_type: Unique identifier of the test line localization type
        box_type: Unique identifier of the test box localization type
        margins: Width/height of the margins to apply (pixels). None if should be ignored.
        image_size: Width/height of the image size forced on the localization graphic.
    """

    # Define mapping from type unique ID and dtype string
    LOCALIZATION_TYPES_INT_TO_DTYPE = {
        dot_type: 'dot',
        line_type: 'line',
        box_type: 'box'}

    # Create interface
    tator_api = tator.get_api(host, token)
    media = tator_api.get_media(media_id)

    # Create the localizations and send it over to the server
    if media.num_frames is not None:
        FRAME_NUMBER = random.randint(0, media.num_frames - 1)
    else:
        FRAME_NUMBER = 0

    NUM_LOCALIZATIONS = 10
    localization_list = []
    for localization_type in LOCALIZATION_TYPES_INT_TO_DTYPE:
        for idx in range(NUM_LOCALIZATIONS):

            localization = _random_localization(
                project=project,
                media_id=media_id,
                dtype=LOCALIZATION_TYPES_INT_TO_DTYPE[localization_type],
                type_id=localization_type,
                frame=FRAME_NUMBER)

            localization_list.append(localization)

    response = tator_api.create_localization_list(project, body=localization_list)

    # Generate the truth information for unit testing
    truth_graphic_info = {}
    for localization_id, localization in zip(response.id, localization_list):
        truth_graphic_info[localization_id] = _generate_truth_info(
            localization_datum=localization,
            media_width=media.width,
            media_height=media.height,
            dtype=LOCALIZATION_TYPES_INT_TO_DTYPE[localization['type']],
            margins=margins)

    # Cycle through the localizations, create the thumbnail and compare the image sizes
    for localization_id in truth_graphic_info:

        truth_width = truth_graphic_info[localization_id][0]
        truth_height = truth_graphic_info[localization_id][1]

        if margins is None:
            if image_size is None:
                image_path = tator_api.get_localization_graphic(localization_id)
            else:
                image_size_str = f'{image_size[0]}x{image_size[1]}'
                image_path = tator_api.get_localization_graphic(localization_id, force_scale=image_size_str)
        else:
            if image_size is None:
                image_path = tator_api.get_localization_graphic(
                    localization_id,
                    use_default_margins=False,
                    margin_x=margins[0],
                    margin_y=margins[1])
            else:
                image_size_str = f'{image_size[0]}x{image_size[1]}'
                image_path = tator_api.get_localization_graphic(
                    localization_id,
                    use_default_margins=False,
                    margin_x=margins[0],
                    margin_y=margins[1],
                    force_scale=image_size_str)

        img = Image.open(image_path)

        if image_size is not None:
            truth_width = image_size[0]
            truth_height = image_size[1]

        assert _ints_almost_equal(img.size[0], truth_width)
        assert _ints_almost_equal(img.size[1], truth_height)

def test_localization_graphic_image(
        host: str,
        token: str,
        project: int,
        image: int,
        dot_type: int,
        line_type: int,
        box_type: int) -> None:
    """ Test localization graphic endpoint with an image

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
        media_id: Unique identifier of media associated with the localization
        dot_type: Unique identifier of the test dot localization type
        line_type: Unique identifier of the test line localization type
        box_type: Unique identifier of the test box localization type

    Create a variety of different localizations
    Create thumbnails from each of them using default margins
    Create thumbnails from each of them using explicit margins
    Create thumbnails from localizations that have a small width/height
    Create thumbnail from localization with margins that expand the media's dimensions

    """

    _perform_random_sizes_test(
        host=host,
        token=token,
        project=project,
        media_id=image,
        dot_type=dot_type,
        line_type=line_type,
        box_type=box_type)

    _perform_random_sizes_test(
        host=host,
        token=token,
        project=project,
        media_id=image,
        dot_type=dot_type,
        line_type=line_type,
        box_type=box_type,
        margins=(100, 100))

    _perform_random_sizes_test(
        host=host,
        token=token,
        project=project,
        media_id=image,
        dot_type=dot_type,
        line_type=line_type,
        box_type=box_type,
        margins=(10, 10),
        image_size=(50, 50))

    _perform_specific_box_size_test(
        host=host,
        token=token,
        project=project,
        media_id=image,
        box_type=box_type,
        x=0.5,
        y=0.5,
        width=1,
        height=1)

    _perform_specific_box_size_test(
        host=host,
        token=token,
        project=project,
        media_id=image,
        box_type=box_type,
        x=0.5,
        y=0.5,
        width=1,
        height=10)

    _perform_specific_box_size_test(
        host=host,
        token=token,
        project=project,
        media_id=image,
        box_type=box_type,
        x=0.5,
        y=0.5,
        width=10,
        height=1)

    _perform_specific_box_size_test(
        host=host,
        token=token,
        project=project,
        media_id=image,
        box_type=box_type,
        x=0.0,
        y=0.0,
        width=50,
        height=50,
        margins=(10000,10000))

def test_localization_graphic_video(
        host: str,
        token: str,
        project: int,
        video: int,
        dot_type: int,
        line_type: int,
        box_type: int) -> None:
    """ Test localization graphic endpoint with a video

    Args:
        host: Project URL
        token: User token used for connecting to the host
        project: Unique identifier of test project
        media_id: Unique identifier of media associated with the localization
        dot_type: Unique identifier of the test dot localization type
        line_type: Unique identifier of the test line localization type
        box_type: Unique identifier of the test box localization type

    Create a variety of different localizations over a few different frames
    Create thumbnails from each of them using default marings
    Create thumbnails from each of them using explicit marings
    Create thumbnails from localizations that have a small width/height
    Create thumbnail from localization with margins that expand the media's dimensions

    """

    _perform_random_sizes_test(
        host=host,
        token=token,
        project=project,
        media_id=video,
        dot_type=dot_type,
        line_type=line_type,
        box_type=box_type)

    _perform_random_sizes_test(
        host=host,
        token=token,
        project=project,
        media_id=video,
        dot_type=dot_type,
        line_type=line_type,
        box_type=box_type,
        margins=(100, 100))

    _perform_random_sizes_test(
        host=host,
        token=token,
        project=project,
        media_id=video,
        dot_type=dot_type,
        line_type=line_type,
        box_type=box_type,
        margins=(10, 10),
        image_size=(50, 50))

    _perform_specific_box_size_test(
        host=host,
        token=token,
        project=project,
        media_id=video,
        box_type=box_type,
        x=0.5,
        y=0.5,
        width=1,
        height=1)

    _perform_specific_box_size_test(
        host=host,
        token=token,
        project=project,
        media_id=video,
        box_type=box_type,
        x=0.5,
        y=0.5,
        width=1,
        height=10)

    _perform_specific_box_size_test(
        host=host,
        token=token,
        project=project,
        media_id=video,
        box_type=box_type,
        x=0.5,
        y=0.5,
        width=10,
        height=1)

    _perform_specific_box_size_test(
        host=host,
        token=token,
        project=project,
        media_id=video,
        box_type=box_type,
        x=0.0,
        y=0.0,
        width=50,
        height=50,
        margins=(10000,10000))
