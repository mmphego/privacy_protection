import argparse

import cv2

from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import Cascade
from skimage.filters import gaussian
from skimage.io import imread, imsave


def get_face_rectangle(orig_image, detected_face):
    """
    Extracts the face from the image using the coordinates of the detected image
    """
    # X and Y starting points of the face rectangle
    x, y = detected_face["r"], detected_face["c"]

    # The width and height of the face rectangle
    width, height = (
        detected_face["r"] + detected_face["width"],
        detected_face["c"] + detected_face["height"],
    )

    # Extract the detected face
    face = orig_image[x:width, y:height]
    return face


def merge_blurry_face(original, gaussian_image, detected_face):
    # X and Y starting points of the face rectangle
    x, y = detected_face["r"], detected_face["c"]
    # The width and height of the face rectangle
    width, height = (
        detected_face["r"] + detected_face["width"],
        detected_face["c"] + detected_face["height"],
    )

    original[x:width, y:height] = gaussian_image
    return original


def show_image(image, title="Image", cmap_type="gray"):
    plt.figure(figsize=(12, 10))
    # plt.imshow(image, cmap=cmap_type)
    plt.imshow(image)
    plt.title(title)
    plt.axis("on")
    plt.show()


def show_detected_face_obtain_faces(result, detected, title="Face image"):
    plt.figure()
    plt.imshow(result)
    img_desc = plt.gca()
    plt.set_cmap("gray")
    plt.title(title)
    plt.axis("off")

    for patch in detected:
        img_desc.add_patch(
            patches.Rectangle(
                (patch["c"], patch["r"]),
                patch["width"],
                patch["height"],
                fill=False,
                color="r",
                linewidth=2,
            )
        )

    plt.show()
    rostros = [
        result[d["r"] : d["r"] + d["width"], d["c"] : d["c"] + d["height"]]
        for d in detected
    ]
    return rostros


def face_detections(
    image, scale_factor=1.1, step_ratio=1.3, min_size=(10, 10), max_size=(400, 400)
):
    # Load the trained file from data
    trained_file = data.lbp_frontal_face_cascade_filename()

    # Initialize the detector cascade
    detector = Cascade(trained_file)

    # Detect faces with min and max size of searching window
    detected_faces = detector.detect_multi_scale(
        img=image,
        scale_factor=scale_factor,
        step_ratio=step_ratio,
        min_size=min_size,
        max_size=max_size,
    )
    return detected_faces


def blur_faces(image, detected_faces):
    resulting_image = None
    # For each detected face
    for detected_face in detected_faces:
        # Obtain the face rectangle from detected coordinates
        face = get_face_rectangle(image, detected_face)

        # Apply gaussian filter to extracted face
        # Scikit-image
        # blurred_face = gaussian(face, multichannel=True, sigma=(45,45))

        # OpenCV2
        blurred_face = cv2.GaussianBlur(face, (45, 45), cv2.BORDER_DEFAULT)

        # Merge this blurry face to our final image and show it
        resulting_image = merge_blurry_face(image, blurred_face, detected_face)

    return resulting_image


def arg_parser():
    """Parse command line arguments.

    :return: command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input", required=True, type=str, help="Path to an image.",
    )
    # TODO: Add Cascade.detect_multi_scale params
    return parser.parse_args()


if __name__ == "__main__":
    args = arg_parser()
    image = imread(args.input)
    detected_faces = face_detections(image)
    resulting_image = blur_faces(image, detected_faces)
    imsave("Blurred_Faces.jpg", resulting_image)
