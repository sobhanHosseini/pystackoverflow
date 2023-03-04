from dataclasses import dataclass

@dataclass
class InlineKeys:
    actions:str = 'Actions :fast-forward_button:'
    back:str = ':fast_reverse_button: Back'
    answer:str = ':bright_button: Answer'
    follow:str = ':plus: Follow'
    unfollow:str = ':minus: Unfollow'
    like:str = ':red_heart: Like'
    