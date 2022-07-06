class StateMachine:
  def __init__(self):
    self.current_user = None
    
  def change_state(self, new_state: str or None):
    self.current_user = new_state
    
  def current_state(self):
    return self.current_user
  