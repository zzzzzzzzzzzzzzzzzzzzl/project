# im just going to put bits of code here that are incomplete or a save point incase i need it in the future

class ball:
    def __init__(self,p,v):
        self.p=p#ball position x,y
        self.v=v#ball velocity x,y
        self.grounded=False# if the ball has enough velocity to bounce grounded will be false
        self.still=False# if the ball is grounded it will slow x velocity
        self.z=[self.p[0]-100,self.p[1]]
        
 
        
        self.bone=((self.z[0]-self.p[0])**2+(self.z[1]-self.p[1])**2)# distance from hinge to ball
       # self.hinge=(p[0]+z[0],p[1]+z[1])#point which will not move
        self.hinge=self.z
        self.over=True
   
        
            
    
  
    def swing(self):

        b=self.bone
        h=self.hinge
        x=self.p[0]
        y=self.p[1]
          
        vec=[x-h[0],y-h[1]]
        xs=vec[0]**2
        ys=vec[1]**2
        xr=(xs/b)
        yr=(ys/b)
        
        self.v[0]+=1*xr
        tv=sum(self.v)
        v1=xr*tv
        v2=yr*tv
        print(xr,yr)
        
      #  print(v1,v2,"test",vec)
        vec.append(negpos(vec[0]))
        vec.append(negpos(vec[1]))
        x+=v1
        y+=v2
        if v1>=v2 and xr+yr<=1.1:
            self.p[1]+=v1
            self.p[0]-=v2
            ys=b-(self.p[0]**2)
            #math.sqrt()
        if v1<v2 and v1<100 and xr+yr<=1.1:
            self.p[0]-=v2
            self.p[1]+=v1
            ys=b-(self.p[0]**2)
