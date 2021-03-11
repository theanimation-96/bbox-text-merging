# bbox-text-merging
This is a python script for finding and evaluating the text nearer to each other or this will get you all text from the image in one line, from left to right sequence.
Before you pass your bounding boxes make sure that you are passing it in right format.

`Here the bounding box should be in left-top and right-bottom formats. eg.(left-side, top-side), (right-side, bottom-side), 'Text')
top coordinate: bottom coordinate : both are constant(minimal difference i.e. Pixel Tolerance) coordinates for in-line text`
 `((1666, 503), (2049, 555), 'Text1'),
  ((1197, 499), (1466, 567), "Text2"),
  ((1478, 507), (1643, 557), 'Text3')`
  
 As you can see top and bottom are constant for in-line text.

Thanks, Enjoy!!!
