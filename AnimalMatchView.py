# See: http://omz-forums.appspot.com/pythonista/post/5883071282806784

import random, sound, ui

font_name = 'ChalkboardSE-Bold'

# Create a list of image names
animals = '''Ant Bear_Face Bug Chicken Cow_Face Dog_Face Elephant Fish
Frog_Face Honeybee Pig_Face Snail Snake Whale Tiger_Face Rabbit_Face'''.split()

# convert an image name to an animal name with spaces between each letter
def animal_name(image_name):
    name = image_name.partition('_')[0].lower()
    name = { 'bug': 'caterpillar',
             'honeybee': 'bee' }.get(name, name)
    return ' '.join(name)  # add spaces between each letter

class AnimalMatchView(ui.View):
    def __init__(self):
        self.hidden = True
        self.current_animal = None
        self.score = 0
        self.present(orientations=['landscape'], hide_title_bar=True)
        self.add_subview(self.close_button())
        self.add_subview(self.make_name_label())
        self.add_subview(self.make_score_label())
        # Setup screen with top 200 pixels reserved for text
        x, y, w, h = self.bounds
        self.col_width = w / 4
        self.row_height = (h - 200) / 4
        for animal in animals:
            self.add_subview(self.make_image_button(animal))
        self.refresh_game()
        self.hidden = False

    @property
    def animals(self):
        return [v for v in self.subviews
             if v.name and isinstance(v, ui.Button)]

    @property
    def a_different_animal(self):
        animal = random.choice(self.animals)
        if animal == self.current_animal:
            return self.a_different_animal
        return animal

    def refresh_game(self):
        self.shuffle_image_locations()
        self.current_animal = self.a_different_animal
        self['name'].text = animal_name(self.current_animal.name)
        self['score'].text = 'Score = %d' % self.score

    def close_action(self, sender):
        self.close()

    def close_button(self):
        button = ui.Button(title='X')
        button.x = self.width - button.width
        button.y = button.height / 2
        button.action = self.close_action
        button.font = ('<system-bold>', 20)
        return button

    def make_name_label(self):
        label = ui.Label(name='name')
        label.alignment = ui.ALIGN_CENTER
        label.width = self.width * 0.6
        label.center = self.center
        label.font = (font_name, 64)
        label.y = 100 - label.height / 2
        return label

    def make_score_label(self):
        label = ui.Label(name='score')
        label.font = (font_name, 32)
        label.width = self.width * 0.2
        label.x = 20
        label.y = 100 - label.height / 2
        return label

    def make_image_button(self, image_name='Snake'):
        frame = 0, 0, self.col_width, self.row_height
        button = ui.Button(frame=frame, name=image_name)
        button.action = self.animal_action
        button.background_image = ui.Image.named(image_name)
        return button

    def shuffle_image_locations(self):
        #random.shuffle(self.subviews)  # tuple :-(
        views = self.animals
        random.shuffle(views)
        for i, view in enumerate(views):
            x, y, w, h = view.frame
            view.frame = ((i % 4) * self.col_width,
                          (i / 4) * self.row_height + 190, w, h)

    def animal_action(self, animal):
        if animal == self.current_animal:
            sound.play_effect('Powerup_1')
            self.score += 1
            self.refresh_game()
        else:
            sound.play_effect('Error')
            self.score -= 1
            self['score'].text = 'Score = %d' % self.score

AnimalMatchView()
