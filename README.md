# SE-Object-Generator
A very basic, very lazy, very barebones randomized system generator  script for SpaceEngine version 0.991.45.1940
requires python 3

# Usage/Examples

in a terminal window, change to the directory where generator.py is installed and run it. Provde a number of random systems to generate, and or the optional generation arguments. The results will appear neatly formatted in a file called "test.cfg"

```bash
python generator.py -n (options)
```

If you wanted to create a batch of 1000 new systems quickly 

```bash
 python generator.py 100 
```

Or, if you wanted to generate 10,000 comets for a system "New Star" that already exists.

```bash
 python generator.py 10000 -c -p "New Star"
```

## Parameters and Options 

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `number -n` | `int` | **Required**. The number of systems to generate |


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `comets -c` | `bool` | **Optional** Generate comets only (for systems that already exist) |


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `ParentBody -p` | `string` | **Optional (required by -comets)** The ParentBody to generate comets for|




## Acknowledgements

 - [Offical SE Scripting manual](https://spaceengine.org/manual/user-manual)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)


