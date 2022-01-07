"""Do the image"""
import time
from dataclasses import dataclass
from typing import Iterable
import os
import logging

import easygui
from PIL import Image


class NotRGBRGBA(Exception):
    """dumb."""

    def __str__(self) -> str:
        """are."""
        return 'you are not supposed to see this'


STI_NAME = 'sti_names.txt'


def open_file(file: str) -> str:
    """Return file contents of any plain text file in the directory file.
    """
    with open(file) as f:
        file_text = f.read()
    return file_text


def check_allowed_suffix(filename: str, allowed_suffix: Iterable) -> bool:
    """Return true if filename is one of the formats in allowed_suffix.
    """
    for suffix in allowed_suffix:
        if filename[-len(suffix):] == suffix:
            return True
    else:
        return False


@dataclass
class Preferences:
    """A class representing the preferences of this module.
    """
    image_dim: tuple[int, int]
    export_filetype: str = '.jpg'
    process_type: str = 'crop'
    allowed_dir_names: tuple[str] = ('.png', '.jpg')


def import_image(directory: str) -> Image:
    """Import image given directory.
    """
    # if dir[-4:] != '.png':
    # image = Image.open(dir)
    # return image
    image = Image.open(directory)
    if image.mode == 'RGB':
        return image
    elif image.mode == 'RGBA':
        image.load()  # required for png.split()

        background = Image.new("RGB", image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
        return background
    else:
        raise NotRGBRGBA


def transform_image(image: Image, prefs: Preferences) -> None:
    image.thumbnail(prefs.image_dim, Image.ANTIALIAS)
    image.save('testoutfile.jpg', 'JPEG')


# def main() -> None:
#    image_dir = 'sample_image.jpg'
#    prefs = Preferences((425, 320))
#    image = import_image(image_dir)
#    transform_image(image, prefs)


class ImageSystem:
    """A class representing the entire image system.
    """
    prefs: Preferences
    dir_list = list[str]  # not used here
    import_folder_path: str  # the folder you wish to process
    export_folder_path: str  # always export
    images_to_process: list[str]  # list of images to process
    images_to_process_full: list[str]  # that with the dir
    export_image_names: list[str]  # list of STI image names

    def __init__(self) -> None:
        """init bruv
        """
        self.prefs = Preferences((425, 320))
        self.export_folder_path = 'export'
        self.create_new_dir()
        self.import_folder_path = easygui.diropenbox('Select import folder', 'Test')
        self.images_to_process = self.collect_files_from_dir()
        self.export_image_names = self.generate_export_image_names()
        self.images_to_process_full = [self.image_path_to_dir(x) for x in self.images_to_process]
        self.comp_main()

    def comp_main(self) -> None:
        """The entire thing."""
        if len(self.images_to_process_full) < len(self.export_image_names):
            logging.warning('Input folder has less images than total STI images.')
        for raw_image_dir, export_image_name in zip(self.images_to_process_full,
                                                    self.export_image_names):
            try:
                img = import_image(raw_image_dir)
            except NotRGBRGBA:
                continue
            img = img.resize(self.prefs.image_dim)
            # img.thumbnail(self.prefs.image_dim, Image.ANTIALIAS)
            img.save('export\\' + export_image_name, 'JPEG', quality=100, subsampling=0)
            logging.info(f'Saved image of filename {export_image_name}')

    def generate_export_image_names(self) -> list[str]:
        """Return list of STI image names.
        """
        return ['Airplane.jpg', 'ApplePicking.jpg', 'ArtMuseum.jpg', 'AvocadoToast.jpg', 'BabyAnnouncement.jpg',
                'Barn.jpg', 'Baseball.jpg', 'Basketball.jpg', 'Bat.jpg', 'BathroomStall.jpg', 'BBQ.jpg', 'Beach.jpg',
                'Bear.jpg', 'Bicycle.jpg', 'BirthdayParty.jpg', 'Bonfire.jpg', 'BookStore.jpg', 'Boxing.jpg',
                'BubbleBath.jpg', 'Cabin.jpg', 'Camping.jpg', 'Cat.jpg', 'Chimpanzee.jpg', 'Chinese.jpg',
                'CoffeeShop.jpg', 'CompactCar.jpg', 'ConcertStage.jpg', 'Condo.jpg', 'CondoInterior.jpg',
                'Convertible.jpg', 'Dentist.jpg', 'Desert.jpg', 'DMV.jpg', 'Dog.jpg', 'Dolphin.jpg', 'Elephant.jpg',
                'EngagementRing.jpg', 'FarmHouse.jpg', 'FeetOnBeach.jpg', 'Ferret.jpg', 'Field.jpg', 'Fireworks.jpg',
                'Football.jpg', 'Forest.jpg', 'Funeral.jpg', 'GasStation.jpg', 'Giraffe.jpg', 'Goldfish.jpg',
                'Gorilla.jpg', 'Graduation.jpg', 'Guacamole.jpg', 'Guacamole.png', 'Gym.jpg', 'Gyro.jpg',
                'Hamburger.jpg', 'Hockey.jpg', 'HomeRepair.jpg', 'Horse.jpg', 'HorseRace.jpg', 'HotAirBalloon.jpg',
                'HotDogs.jpg', 'HouseParty.jpg', 'IceCream.jpg', 'Igloo.jpg', 'Indian.jpg', 'Island.jpg', 'Jeep.jpg',
                'Jungle.jpg', 'Kite.jpg', 'Kittens.jpg', 'Laundromat.jpg', 'Lion.jpg', 'London.jpg', 'Mansion.jpg',
                'MeatSkewer.jpg', 'Meditation.jpg', 'Mexican.jpg', 'Minivan.jpg', 'Moose.jpg', 'Motel.jpg',
                'Motorcycle.jpg', 'Mountains.jpg', 'MovieTheater.jpg', 'Moving.jpg', 'Museum.jpg', 'Nascar.jpg',
                'NewYorkCity.jpg', 'Office.jpg', 'Orangutan.jpg', 'Parade.jpg', 'Paris.jpg', 'Park.jpg',
                'ParkingTicket.jpg', 'PickupTruck.jpg', 'Pig.jpg', 'Pizza.jpg', 'PoolParty.jpg', 'PostOffice.jpg',
                'Puppies.jpg', 'Rabbit.jpg', 'Rainstorm.jpg', 'Rollerblades.jpg', 'RollerCoaster.jpg',
                'RomanticGetaway.jpg', 'Russia.jpg', 'Sailboat.jpg', 'Salad.jpg', 'Salmon.jpg', 'SanFrancisco.jpg',
                'Segway.jpg', 'SemiTruck.jpg', 'ShootingStar.jpg', 'Skyscraper.jpg', 'Snake.jpg', 'Soccer.jpg',
                'Spider.jpg', 'StationWagon.jpg', 'Statue.jpg', 'Steak.jpg', 'SubwayCar.jpg', 'Suitcase.jpg',
                'Sunset.jpg', 'Tennis.jpg', 'Traffic.jpg', 'Train.jpg', 'Vegas.jpg', 'Volleyball.jpg', 'Voting.jpg',
                'VR.jpg', 'Wedding.jpg', 'Wrestling.jpg', 'WritingDesk.jpg', 'Yoga.jpg']
        # this method of pasting lists is dumb

        # image_list_str = open_file(STI_NAME)
        # image_list = image_list_str.split('\n')
        # return image_list

    def create_new_dir(self) -> None:
        """Create the export directory. If it already exists, do nothing.
        """
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, self.export_folder_path)
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        else:
            logging.warning('export path already exists')

    def collect_files_from_dir(self) -> list[str]:
        """Return a list of filenames from a directory, and then
        only include images within the allowed formats.
        """
        arr = os.listdir(self.import_folder_path)
        allowed_img_files = []
        for filename in arr:
            if check_allowed_suffix(filename, self.prefs.allowed_dir_names):
                allowed_img_files.append(filename)
        return allowed_img_files

    def image_path_to_dir(self, image_path: str) -> str:
        """Return the full directory path for an image in the import folder.
        """
        return self.import_folder_path + '\\' + image_path


def try_everything() -> None:
    ImageSystem()


if __name__ == '__main__':
    try:
        try_everything()
        print('Exporting complete. Closing in 4 seconds.')
    finally:
        time.sleep(4)
