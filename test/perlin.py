import pygame 
import math

def findnoise2(x,y):
	n = int(x) + int(y) * 57
	allf = 0xFFFFFFFF
	an = (n << 13) & allf
	n = (an ^ n) & allf
	nn = (n*(n*n*60493+19990303)+1376312589)&0x7fffffff
	return 1.0-(float(nn)/1073741824.0);

def interpolate( a, b, x):
	ft = float(x * 3.1415927)
	f = float((1.0-math.cos(ft))* 0.5)
	return a*(1.0-f)+b*f;

def noise(x,y):
    floorx = float(int(x))
    floory = float(int(y))
    s=findnoise2(floorx,floory) 
    t=findnoise2(floorx+1,floory)
    u=findnoise2(floorx,floory+1) 
    v=findnoise2(floorx+1,floory+1)
    int1=interpolate(s,t,x-floorx) 
    int2=interpolate(u,v,x-floorx)
    return interpolate(int1,int2,y-floory) 

def main():
	pygame.init()
	screen = pygame.display.set_mode((600, 480))
	clock = pygame.time.Clock()
	noiseimage = pygame.Surface(screen.get_size())
	noiseimage.fill((120,40,120))
	scale1 = 2.0
	scale2 = 4.0
	scale3 = 8.0
	for w in range(0, noiseimage.get_width()):
		for h in range(0, noiseimage.get_height()):
			i = int((noise(w/scale1,h/scale1)+1.0) * 42)
			i += int((noise(w/scale2,h/scale2)+1.0) * 42)
			i += int((noise(w/scale3,h/scale3)+1.0) * 42)
			if(i>255):
				i=255
			if(i<0):
				i=0
			noiseimage.set_at((w,h),(i,i,i))
	screen.blit(noiseimage, (0,0))
	pygame.display.flip()
	while 1:
		clock.tick(60)
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                return
        screen.blit(noiseimage, (0,0))
        pygame.display.update()

if __name__ =='__main__': 
  main()