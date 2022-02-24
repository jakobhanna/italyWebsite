# Images
Instead, we chose to apply an obsolete image compression technique called “dithering”. The number of colours in an image, combined with its file format and resolution, contributes to the size of an image. Thus, instead of using full-colour high-resolution images, we chose to convert all images to black and white, with four levels of grey in-between. 

These black-and-white images are then coloured according to the pertaining content category via the browser’s native image manipulation capacities. Compressed through this dithering plugin, images featured in the articles add much less load to the content: compared to the old website, the images are roughly ten times less resource-intensive.(https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website/)

Bayesian Ordered Dithering (https://homebrewserver.club/low-tech-website-howto.html#configuring-the-webserver) -> pelican plugin (https://github.com/lowtechmag/solar-plugins)

# Resource saving
All resources loaded, including typefaces and logos, are an additional request to the server, requiring storage space and energy use. Therefore, our new website does not load a custom typeface and removes the font-family declaration, meaning that visitors will see the default typeface of their browser.(https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website/)

# Logs, analysing
No third partie, only local logs

# Texts
written in markdown (md)
