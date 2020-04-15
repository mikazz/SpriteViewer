import os

verbose = False
vprint = print if verbose else lambda *a, **k: None


def get_asset(walk_dir):
    """
        Example For Images (same goes for sounds):

        Put your *.png 's inside directory, the name of directory
        indicates the name of animation so it's necessary, to build a dictionary out of it
        Then, call the function with:

        walk_dir - which specifies the directory to search for animation directories
        i.e: "img\player"

        Method will return dictionary based on subdirectories (key) and files inside them (values as single list)
        {
            subdir_1 : ["filepath_1.png", "filepath_2.png", "filepath_3.png"]
            subdir_2 : ["filepath_1.png", "filepath_2.png", "filepath_3.png"]
        }

        import pprint
        pprint.pprint(get_sprites("img\player"), width=1)

        ------------ Example Usage: ------------

        sprites = sprite_loader.get_sprites("img\player")
        self.images = []
        walk_sprites = sprites.get("walk", None)

        for sprite in walk_sprites:
            self.images.append(pygame.image.load(sprite))
    """

    if os.path.exists(walk_dir) is False:
        print(f"No such directory {walk_dir}")
        return


    dictionary = {}
    subdirs_list = []
    all_paths_list = []

    vprint('walk_dir = ' + walk_dir)
    vprint('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

    for root, subdirs, files in os.walk(walk_dir):
        # subdirs - list of all subdir
        vprint('--\nroot = ' + root)

        for subdir in subdirs:
            vprint('\t- subdirectory ' + subdir)
            subdirs_list.append(subdir)

        paths_list = []  # reset when done with single directory

        for filename in files:
            file_path = os.path.join(root, filename)
            vprint('\t- file %s (full path: %s)' % (filename, file_path))
            paths_list.append(file_path)  # Add head directory data "data\\" +

        if paths_list:
            all_paths_list.append(paths_list)

    for i, j in zip(subdirs_list, all_paths_list):
        dictionary[i] = j

    return dictionary
