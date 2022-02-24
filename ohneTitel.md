# Images
Instead, we chose to apply an obsolete image compression technique called “dithering”. The number of colours in an image, combined with its file format and resolution, contributes to the size of an image. Thus, instead of using full-colour high-resolution images, we chose to convert all images to black and white, with four levels of grey in-between. 

These black-and-white images are then coloured according to the pertaining content category via the browser’s native image manipulation capacities. Compressed through this dithering plugin, images featured in the articles add much less load to the content: compared to the old website, the images are roughly ten times less resource-intensive.(https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website/)

Bayesian Ordered Dithering (https://homebrewserver.club/low-tech-website-howto.html#configuring-the-webserver) -> pelican plugin (https://github.com/lowtechmag/solar-plugins)

blend images (https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode)
These black and white images are then colored according to the pertaining content category (Low-tech Solution, High-tech Problems, or Obsolete Technology) via CSS blend-modes. The hard-light overlay technique allows only the white parts of the image against its background, allowing the color behind the image to colorize it.

For background images, we can use the background-color. For content images in articles, we will need it in a wrapper (coloring the img background does not work.) Fortunately, the format in which the articles are written – in markdown — automatically wraps images specfied in a paragraph tag. These image-wrapping paragraphs were captured via the addressable a Pelican plugin in order to colorize the images. (https://github.com/lowtechmag/solar/wiki/Solar-Web-Design)

image sprites load multiple images as one (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Images/Implementing_image_sprites_in_CSS)

# Weather
JavaScript adds weather-specific CSS classes read from the existing server stats, which pulls weather information from DarkSky.net(https://darksky.net/forecast/41.3829,2.1774/us12/en). The CSS file then sets up the image as a background and adjusts which part of the image to display according to the class. (https://github.com/lowtechmag/solar/wiki/Solar-Web-Design)

# Javascript
Use only self implemted functions etc

# Print styles
necessery?

# Resource saving
All resources loaded, including typefaces and logos, are an additional request to the server, requiring storage space and energy use. Therefore, our new website does not load a custom typeface and removes the font-family declaration, meaning that visitors will see the default typeface of their browser.(https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website/)

# Logs, analysing
No third partie, only local logs

# Texts
written in markdown (md)

# Server
nginx mit leichten Anpassungen (https://homebrewserver.club/low-tech-website-howto.html#configuring-the-webserver)
