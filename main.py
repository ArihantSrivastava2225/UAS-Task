import changecolorregion as module1
import totalredtriinbrownreg as module2
import totalbluetriangles as module3
import totalredtriangles as module4
import totaltrianglesinbrownregion as module5
images=['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png']
n_houses=[]
priority_houses=[]
priority_ratio=[]
for image in images:
    module1.changeColorRegion(image)
    HTr = module4.totalRed(image)
    HTb = module3.totalBlue(image)
    HT = HTr + HTb
    Hb = module5.housesinBurntGrass(image)
    Hg = HT - Hb
    Hbr = module2.redhousesinBurntGrass(image)
    Hbb = Hb - Hbr

    Hgr = HTr - Hbr
    Hgb = Hg - Hgr
    xn_houses=[Hb, Hg]
    xpriority_houses= [Hbr*1 + Hbb*2, Hgr*1 + Hgb*2]
    xpriority_ratio = xpriority_houses[0]/xpriority_houses[1]
    n_houses.append(xn_houses)
    priority_houses.append(xpriority_houses)
    priority_ratio.append(xpriority_ratio)

print("n_houses : ")
print(n_houses)
print("priority_houses : ")
print(priority_houses)
print("priority_ratio : ")
print(priority_ratio)
priority_arrange=sorted(priority_ratio, reverse=True)
# print(priority_arrange)
ind=[]
for i in priority_arrange:
    for j in priority_ratio:
        if i==j:
            ind.append(priority_ratio.index(j))

# print(ind)
priority_images = []
for i in ind:
    priority_images.append(images[i])

print("priority_images : ")
print(priority_images)
