title: Webpack for Mortals
author: Chris Penner
date: August 29th
tags: programming javascript
description: Webpack is a brilliant tool, but getting started has a steep learning curve.

Webpack is a brilliant tool, but getting started has a steep learning curve.
Articles all across the internet are telling us to build Single Page Applications
and to optimize our bundles and that we'll end up with an amazing user experience,
but they never actually say HOW to do it. We're going to look at how to set up
a Single Page Application using webpack.

So first, what is webpack and how can it help you? Webpack's primary concern is
'bundling' all of your static assets (javascript, css, etc.) into one big
file. While it's a handy thing to do, packing things up into a big file isn't
really anything to write home about. Webpack's real popularity has come from
its extensibility and its ability to perform transformations on your code
during the bundling process. Think of it as an extensible pre-processor for
your code. Almost anything that can be done at 'build' time can be accomplished
through webpack. It can replace grunt and gulp as build tools if you so choose.

# Getting started

Webpack uses a configuration file (called **webpack.config.js** by convention).
This is a normal javascript file, so you can execute code here, check
environment variables, whatever you need to do. The only requirement is that at
the end of the process a configuration object is exported. The
webpack.config.js file is written using the commonjs style of exports, but
don't worry about that if you don't know what it means. Here's a look at a
barebones minimal webpack config.


