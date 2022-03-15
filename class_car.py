class Car():


  #positional argument: 정의한 위치대로 개입
    #ex)def b(a,c):
  #keyword argument: 순서를 무시하고 입력
    #ex)def a(nick="닉",cow="카우"):

  # def start(self): #method:function of class
  #   #method의 첫 번째 인자로 instance가 자동으로 부여된다
  #   #따라서 인자를 비워두지 말고 관례상 "self"로 둘 것.
  #   print(self.doors)    
  #   print("I started")
  def __str__(self):#자동적으로 있던 method 함수:class를 str형태로 변환해주는함수
    return f"Car with {self.wheels} wheels"

  def __init__(self, **kwargs):
    #instance의 변수 설정, 참조
    self.wheels=4
    self.doors=4
    self.windows=4
    self.seats=4
    self.color=kwargs.get("color","black")
    self.price=kwargs.get("price","$20")


class Convertible(Car): #Car를 상속(inherit)

  def __init__(self, **kwargs):
    super().__init__(**kwargs) #상위 클래스의 "수정가능한" 키워드인자 상속 kwargs안쓰면 default값으로상속됨
    self.time=kwargs.get("time",10)

  
  def take_off(self):
    return "taking off"

  def __str__(self):
    return f"Car with no roof"

porche=Convertible(color="green",price="$40")
print(porche.color)
