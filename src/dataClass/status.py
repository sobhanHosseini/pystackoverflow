from dataclasses import dataclass

@dataclass
class Status:
    PREP:str = ':yellow_circle: Typing...'
    DRAFT:str = ':white_circle: Draft'
    CLOSED:str = ':red_circle: Closed'
    OPEN:str = ':green_circle: Open'
    DELETED:str = ':wastebasket: Deleted'
    RESOLVED:str = ':check_mark_button: Resolved'
   