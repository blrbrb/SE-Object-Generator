from __future__ import print_function
import random 
import json 
import argparse
import itertools
import os 
from sys import exit

parser = argparse.ArgumentParser(
                    prog = 'se Star Generator',
                    description = 'generate systems of stars (not realistic very barebones) very poorly written in general. Meant as a quick lazy fix',
                    epilog = 'Among Us')

parser.add_argument('number', metavar='n', type=int, default=1, help='number of systems to generate')    
parser.add_argument('-c','--comets',default=False, help="generate comets only", action='store_true')
parser.add_argument('-p','--ParentBody', metavar='p', type=str) 
args = parser.parse_args()


def write_data():
    
    with open("test.cfg", "a") as outfile:
     if args.comets: 
        print('writing system(s) with procedurally generated comets... \n')
        for i in systems:
          outfile.write("Comet "f'"{args.ParentBody}'f'{random.randint(0,1000000)}"')
          outfile.write("\n { \n")
        
           
            #write the basic star properties first 
          if 'Basic' in i:
           for key in i['Basic'].keys():
             outfile.write(f"{'':<5}"f"{key:<30}{i['Basic'][key]:<40}" + "\n")  
           outfile.write('\n')   
           
           
        
          if 'Orbit' in i:
                   
                    outfile.write(f"{'':<5}""Orbit ")
                    outfile.write('\n'f"{'':<5}"'{ \n')
                    for key in i['Orbit'].keys():
                     outfile.write(f"{'':<6}"f"{key:<30}{i['Orbit'][key]:<40}" + "\n") 
                    outfile.write(f"{'':<5}"'} \n')
                    

        #finish off nice and clean by leaving a newline, for appending to the file in the future (visual coherence is important for the SE format)
        outfile.write('} \n')
        return
     

    for i in systems:
        outfile.write("Star ")
        outfile.write(f'"{star_name}"')
        outfile.write("\n { \n")

        for key in i.keys():
            write_string = (f"{'':<5}"f"{key:<30}{i[key]:<40}"); 
            outfile.write(write_string + "\n") 
            write_string = ''
            #outfile.write(str(  i[key]) + "\n") 
    
    outfile.write('} \n')
        #for value in i.values():
           # outfile.write(str(value) + "\n")
        #outfile.write(str("    MassSol  ") + systems[system]["MassSol"] + '\n')
        #outfile.write(str("    Dist  ") + Star["MassSol"] + '\n')
        #outfile.write(str("    RA  ") + Star["MassSol"] + '\n')
        #outfile.write(str("    Dec  ") + Star["MassSol"] + '\n')
    #outfile.write(obj)









n = args.number 
f = open("test.se", "a")



systems = [{}] * args.number 
orbits = [{}] * args.number
minimum_dist =  5.0891420615012004e9
maximum_dist = 5.0891420615012204e9

minimum_RA = 6.497717000001
maximum_RA = 6.497717
minimum_Dec = -9.0374000001
maximum_Dec = -9.037406
minimum_radius = 0.12
maximum_radius = 1800

Classes = ["O", "B", "A", "F", "G", "K", "M", "Q", "WD"]
CometTypes = ["P", "C"]

#names =["alicorn", "amorae", "amythest", "apple", "aquila", "arboreal", "asterion", "aurora", "bird", "blosom", "canter", "canus", "carapace", "celestia", "celestial", "cervae", "cervus", "charm", "cheval", "cheveux", "chiro", "chiroptera", "chrysalis", "clop", "cloud", "colt", "comet", "courant", "crystal", "cursed", "deer", "diamond", "discord", "dog", "enchanted", "equestrian", "equid", "equine", "equus", "errant", "filly", "floating", "flora", "flowena", "foal", "froggy", "gardens", "gemstone", "glimmer", "green", "greneclyf", "griffon", "gumdrop", "gusty", "harmonic", "harmony", "heart", "hearth", "heartshine", "hellquill", "hippogriff", "honesty", "hooves" "horn" "horse" "kirin" "lumeire" "luna" "lunar" "magic" "mare" "mark" "marmalade" "moon" "olenia" "orange" "paard" "pegasus" "pegusae" "pie" "pinkie" "pony" "quill" "rainbow" "rainbows" "rarity" "red" "reindeer" "rila" "seapony" "shimmer" "siren" "sirens" "sisters" "solar" "sparkle" "spell" "stallion" "starlight" "starry" "steed" "summer' sun sunset swamp tail tirek tropeau trot twilight unicorn vexae vexii vexis whinny windigo wingbardy wings yak", "gryffon zebra zebrica zephyr"]

if args.comets: 
    print('writing')
    for i in range(args.number): 
        systems[i] ={
                "Basic": {
                "ParentBody" : args.ParentBody,
                "CometType" : random.choice(CometTypes),
                "SlopeParam" : random.randint(1, 20),
                "Radius" : random.uniform(1, 100),
                },
                'Orbit':
                {
                    "RefPlane" : "Ecliptic",
                    "Epoch" : random.uniform( 2449400.5,2459706.5),
                    "Eccentricity": random.uniform(0.125309, 1.00002),
                    "Inclination" : random.uniform(0, 360),
                    "AscendingNode"	: random.uniform(0, 360),
		            "ArgOfPericenter" : random.uniform(0, 360),
		            "MeanAnomaly" :	0
		          

                }
            }
 
    write_data()
    exit
                
    
            
        


if args.comets == None:
    for i in range(n):
        print(n)
        systems[i] = {
            "Basic": {
        "MassSol" : random.uniform(0.08, 50),
        "Class" : random.choice(Classes), 
        "RadSol" : random.uniform(minimum_radius, maximum_radius), 
        "Dist": random.uniform(minimum_dist, maximum_dist),
          "RA": random.uniform(minimum_RA, maximum_RA),
         "Dec":  random.uniform(minimum_Dec, maximum_Dec)
            }
     }
    


star_name ="test"
    #systems.append(Star)


obj = json.dumps(systems, indent=3)




    
  