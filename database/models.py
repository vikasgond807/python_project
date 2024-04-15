#Class model for Goal

class Goal:
    """Goal class

    params: 
    title:      string
    description:string
    end_date    :Datetime
    remark      :string
     """
    def __init__(self,title,description,end_date,remark=None):
        self.title=title
        self.desc=description
        self.end_date=end_date
        self.remark=remark


    def __repr__(self) -> str:
        return f"Title: {self.title}  Description: {self.desc}  Deadline: {self.end_date}  Remark: {self.remark}"
