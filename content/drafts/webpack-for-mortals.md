title: Webpack for Mortals
author: Chris Penner
date: August 29th
tags: programming javascript
description: Webpack is a brilliant tool, but getting started has a steep learning curve.

Webpack is a brilliant tool, but getting started has a steep learning curve.
This article is about what I wish I'd known when I started with webpack. We'll
take a practical approach and look through an honest-to-goodness real webpack
file I'm using in one of my projects. We'll also look at how to build a webpack
configuration for a single page application, this is where webpack really
shines, unfortunately there are very few resources on how to set this up (and
even fewer that explain how it works).

So first, what is webpack and how can it help you? Webpack's primary concern is
'bundling' all of your static assets (javascript, css, etc.) into one big
chunk. While it's a handy thing to do, packing things up into a big file isn't
really anything to write home about. Webpack's real popularity has come from
its extensibility and its ability to perform transformations on your code
during the bundling process. Think of it as an extensible pre-processor for
your code. Almost anything that can be done at 'build' time can be accomplished
through webpack. It can replace grunt and gulp as build tools if you so choose.

In this walkthrough we'll look at making a simple bundle out of all of our
javascript dependencies, transpiling from ES6 to ES5 along the way. We'll also
compile our Sass files into CSS including them into our bundle. And lastly
we'll look at how we can leverage webpack to allow users to better cache our
bundles.

# Getting started

Webpack uses a configuration file (called **webpack.config.js** by convention).
This is a normal javascript file, so you can execute code here, check
environment variables, whatever you need to do. The only requirement is that at
the end of the process a configuration object is exported. The
webpack.config.js file is written using the commonjs style of exports, but
don't worry about that if you don't know what it means. Here's a look at a
barebones minimal webpack config.


