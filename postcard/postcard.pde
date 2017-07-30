PImage mainartwork, greetings;

String[] mainartworks = 
{
"testpostcard.jpg",
"testpostcard1.jpg",
"testpostcard2.jpg",
"testpostcard3.jpg",
"testpostcard4.jpg",
"testpostcard5.jpg",
};


void setup() {
  noLoop();
  size(500, 600);
  
  // main image
  mainartwork = loadImage("artworks/"+mainartworks[(int)random(mainartworks.length)]);
  mainartwork.resize(width, 0);
  image(mainartwork, 0, 0);
  
  // text
    greetings = loadImage("greetings.png");
  greetings.resize(int(width*.5), 0);
  image(greetings, 20, 20);
  
  fill(255);
  rect(0, height*.5, width, height*.5);
  
  stroke(0);
  line(width/2, height/2+ 20, width/2, height-20);
  rect(width-width/6, height/2+20, width/8, height/8);
  
  for (int i =0; i<4; i++){
    line(width/2+width/12, height-height/4+height/15*i, width-width/12, height-height/4+height/15*i);
  }
  
  
}

void draw() {
}