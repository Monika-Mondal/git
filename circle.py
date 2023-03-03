def circle(r):
  area=3.14*r*r
  peri=2*3.14*r
  return (area,peri)
r=float(input("enter any value"))
a,p=circle(r)
print("Area of circle:",a)
print("Perimeter of circle:",p)
