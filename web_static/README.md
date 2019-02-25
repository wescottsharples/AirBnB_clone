# AirBnB_clone
## web_static
This is the second part of the *AirBnB clone* project for [Holberton School](https://www.holbertonschool.com/). 
### 0-index.html
This is a HTML page that displays a header and footer without using the `style` tag in the `head` tag.

Layout:
- body:
  - no margin
  - no padding
- header:
  - color `#FF0000` (red)
  - height: 70px
  - width: 100%
- footer:
  - color `#00FF00` (green)
  - height: 60px
  - width: 100%
  - text `Holberton School` center vertically and horizontally
  - always at the bottom of the page
### 1-index.html
This is a HTML page that displays a header and a footer by using the `style` tag in the `head` tag. Layout is exactly the same as `0-index.html`.
### 2-index.html
This is a HTML page that diplays a header and a footer by using CSS files. The layout is the same as `1-index.html`. These are the 3 CSS files:
- `styles/2-common.css`: for global style (i.e. the `body` style)
- `styles/2-header.css`: for header style
- `styles/2-footer.css`: for footer style
### 3-index.html
This is a HTML page that displays a header and footer by using CSS files. There is no inline style, no `style` tag in `head` tag, and no `img` tag used.

Layout:
- common:
  - no margin
  - no padding
  - font color: `#484848`
  - font size: 14px
  - font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
  - [icon](LINK HERE) in the browser tab
- header:
  - color: white
  - height: 70px
  - width: 100%
  - border bottom 1px `#CCCCCC`
  - [logo](LINK HERE) align on left and center vertically (20px space at the left)
- footer:
  - color: white
  - height: 60px
  - width: 100%
  - border top 1px `#CCCCCC`
  - text `Holberton School` center vertically and horizontally
  - always at bottom of page
### 4-index.html
This is a HTML page that displays a header, footer, and a filters box with a search button. There is no inline style, no `img` tag, and no `style` tag in the `head` tag.

Layout: (based on `3-index.html`)
- container:
  - between `header` and `footer` tags, add a `div`:
    - classname: `container`
    - max width 1000px
    - margin top and bottom 30px
    - center horizontally
- filter section:
  - tag `section`
  - classname `filters`
  - inside the `.container`
  - color: white
  - height: 70px
  - width: 100% of the container
  - border 1px `#DDDDDD` with radius 4px
- button search:
  - tag `button`
  - text `Search`
  - font size: 18px
  - inside the section filters
  - background color `#FF545F`
  - text color `#FFFFFF`
  - height: 48px
  - width: 20% of the section filters
  - no borders
  - border radius: 4px
  - center vertically and at 30px of the right border
  - change opacity to 90% when mouse is on the button

The 4 CSS files:
- `styles/4-common.css`: for the global style (`body` and `.container` styles)
- `styles/3-header.css`: for header style
- `styles/3-footer.css`: for footer style
- `styles/4-filters.css`: for the filters style
### 5-index.html
This is a HTML page that displays a header, footer, and a filters box. There is no `img` tag, no `style` tag in the `head` tag, and no inline style.

Layout: (based on `4-index.html`)
- locations and amenities filters:
  - tag: `div`
  - classname: `locations` for location tag and `amenities` for amenity tag
  - inside the section filters (same level as the `button` search)
  - height: 100% of the section filters
  - width: 25% of the section filters
  - border right `#DDDDDD` 1px only for the first left filter
  - contains a title:
    - tag: `h3`
    - font weight: 600
    - text `States` or `Amenities`
  - contains a subtitle:
    - tag: `h4`
    - font weight: 400
    - font size: 14px
    - text with fake contents

The 4 CSS files:
- `styles/4-common.css`: for the global style (`body` and `.container` styles)
- `styles/3-header.css`: for the header style
- `styles/3-footer.css`: for the footer style
- `styles/5-filters.css`: for the filters style
### 6-index.html
This is a HTML page that displays a header, footer, and a filters box with dropdown. There is no inline style, no `img` tag, and no `style` tag in the `head` tag.

Layout: (based on `5-index.html`)
- updated Locations and Amenities filter to display a contextual dropdown when the mouse is on the filter `div`:
  - tag `ul`
  - classname `popover`
  - fake text
  - inside each `div`
  - not displayed by default
  - color: `#FAFAFA`
  - width: same as the `div` filter
  - border `#DDDDDD` 1px with border radius 4px
  - no list display
  - Location filter has 2 levels of `ul`/`li`:
    - state -> cities
    - state name displayed in a `h2` tag (font size 16px)

The 4 CSS files:
- `styles/4-common.css`: for the global style (`body` and `.container` styles)
- `styles/3-header.css`: for the header style
- `styles/3-footer.css`: for the footer style
- `styles/6-filters.css`: for the filters style
### 7-index.html
This is a HTML page that displays a header, footer, and filters box with dropdown and results. There is no inline style, no `img` tag, and no `style` tag in the `head` tag.

Layout: (based on `6-index.html`)
- Places section:
  - tag: `section`
  - classname: `places`
  - same level as the filters section, inside `.container`
  - contains a title:
    - tag: `h1`
    - text: `Places`
    - align in the top left
    - font size: 30px
  - contains multiple "Places" as listing (horizontal or vertical):
    - tag: `article`
	- width: 390px
	- padding and margin 20px
	- border `#FF545F` 1px with radius 4px
	- contains the place name:
	  - tag: `h2`
	  - font size: 30px
	  - center horizontally

The 5 CSS files:
- `styles/4-common.css`: for the global style (i.e. `body` and `.container` style)
- `styles/3-header.css`: for the header style
- `styles/3-footer.css`: for the footer style
- `styles/6-filters.css`: for the filters style
- `styles/7-places.css`: for the places style
### 8-index.html
This is a HTML page that displays a header, footer, filter box (dropdown list) and the result of the search. There is no inline style, no `img` tag, and no `style` tag in the `head` tag.

Layout: (based on `7-index.html`)
add more information to a Place `article`:
- price by night:
  - tag: `div`
  - classname: `price_by_night`
  - same color as the place name
  - font color: `#FF545F`
  - border: `#FF545F` 4px rounded
  - min width: 60px
  - height: 60px
  - font size: 30px
  - align: top right (with space)
- information section:
  - tag: `div`
  - classname: `information`
  - height: 80px
  - border: top and bottom `#DDDDDD` 1px
  - contains (aligned vertically):
    - number of guests:
      - tag: `div`
      - classname: `max_guest`
      - width: 100px
      - fake text
      - [icon](LINK HERE)
    - number of bedrooms:
      - tag: `div`
      - classname: `number_rooms`
      - width: 100px
      - fake text
      - [icon](LINK HERE)
    - number of bathrooms:
      - tag: `div`
      - classname: `number_bathrooms`
      - width: 100px
      - fake text
      - [icon](LINK HERE)
  - user section:
    - tag: `div`
    - classname: `user`
    - text `Owner: <fake text>`
    - `Owner` text is in *bold*
  - description section:
    - tag: `div`
    - classname: `description`
The 5 CSS files:
- `styles/4-common.css`: for the global style (i.e. `body` and `.container` style)
- `styles/3-header.css`: for the header style
- `styles/3-footer.css`: for the footer style
- `styles/6-filters.css`: for the filters style
- `styles/8-places.css`: for the places style
