# pgpyui 0.0.4

pgpyui is an add-on module for pygame to create a user interface.

## Installation

```
pip install pgpyui
```

## Usage

### Button

Imports
```python
from pgpyui import button
import pygame
```

Сreating a button
```python
button = button.Button((100, 100), (200, 100), "Some text", func, sprite="sprites/sprite.png")
```

Event handling
```python
button.check_events(event)
```

Drawing
```python
button.draw(window)
```
#
### Text Area

Imports
```python
from pgpyui import textarea
import pygame
```

Сreating a text area
```python
textarea = textarea.TextArea((200, 100), (100, 100), 20, 15, is_enter=False, font="Arial")
```

Event handling
```python
textarea.check_events(event)
```

Drawing
```python
textarea.draw(window)
```

Information output
```python
text: list[str] = textarea.return_texts()
```

#
### Slider

Imports
```python
from pgpyui import slider
import pygame
```

Сreating a slider
```python
slider = slider.Slider((200, 100), (100, 100), 100, orientation="True")
```

Event handling
```python
slider.check_events(event)
```

Drawing
```python
slider.draw(window)
```

Information output
```python
prgrs: int = slider.return_progress()
```

## Documentation

### Button

**Parameters:**

* `position`: The position of the button.
* `size`: The size of the button.
* `text`: The text on the button.
* `function`: The function to be called when the button is clicked.
* `sprite`: A sprite to use for the button (optional).

### TextArea

**Parameters:**

* `position`: The position of the text area.
* `size`: The size of the text area.
* `font_size`: The size of the font.
* `max_symbols`: The maximum number of symbols that can be entered.
* `is_enter`: Whether or not the enter key should be allowed.
* `font`: The name of the font to use (optional).

### Slider

**Parameters:**

* `position`: The position of the slider.
* `size_block`: The size of the block slider.
* `len`: Length of slide.
* `max_symbols`: The maximum number of symbols that can be entered.
* `orientation`: Horisontal or vertical slider. (optional)


## License

MIT

## Author mail

mixail.vilyukov@icloud.com
