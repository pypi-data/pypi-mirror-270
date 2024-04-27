## vbimage is a CLI tool for basic manipulation of images

### Install using pip

```
pip install vbimage
```

### Usage
```
vbimage -h
```

```
Usage: vbimage [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  blur      Adds background to any transparent image
  grid      Adds background to any transparent image
  layer     Replaces any color with other color.
  pixelate  Pixelates any image.
  removebg  Adds background to any transparent image
  render    Creates an image using given size and color.
  stack     Adds background to any transparent image
```

### Subcommands Usage
```
vbimage grid -h
```
```
Usage: vbimage grid [OPTIONS]

  Adds background to any transparent image

Options:
  -i, --inputimage PATH           Front Image  [default: ./main.png]
  -o, --outputimage PATH          Resized output image  [default:
                                  ./main_grided.png]
  -s, --step <INTEGER INTEGER>...
                                  Number of division.  [default: 10, 10]
  -S, --stroke_width INTEGER      Stroke width of the lines.  [default: 2]
  -h, --help                      Show this message and exit.
```
