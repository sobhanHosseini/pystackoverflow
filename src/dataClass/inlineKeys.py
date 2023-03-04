from dataclasses import dataclass

@dataclass
class InlineKeys:
    actions:str = 'Actions'
    back:str = 'Back'
    answer:str = ':bright_button: Answer'
    follow:str = ':plus: Follow'
    unfollow:str = ':minus: Unfollow',
    like:str = ':red_heart: Like'