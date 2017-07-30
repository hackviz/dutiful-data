/*

Processing Sketch generating postcards 
texts from OIA requests, fyi.org.nz
images from DigitalNZ
postmarks from NZpost
cover art from DigitalNZ search for Wellington
stamps from TePapa collection

GovHack 2017 - http://govhack.org.nz/
http://HackViz.Tech

Free Art Licence

contact: govhack@birgitbachler.com
*/

PImage mainartwork, greetings, stamp, postmark;
PFont writeFont;
Table oirs;

int numOutputs = 1;
int count = 0;

void setup() {
  background(255);
  size(500, 600);
  oirs = loadTable("oia_requests_under_250chars.csv");

  while (count<numOutputs) {
    makeMyPostcard();
    String save = "myoutput"+nf(count, 2)+".png";
    println(save);
    save(save);
    count ++;
  }
}

void draw() {
}


void makeMyPostcard() {
  fill(255);
  rect(0, 0, width, height*.5);

  String myimage = "digitalnz_landscape_"+nf(int(random(2879)), 5)+".jpg";

  // main image
  mainartwork = loadImage("artworks/landscapephotos/"+myimage);
  // mainartwork = loadImage("artworks/landscapephotos/digitalnz_landscape_02540.jpg");

  mainartwork.resize(width, 0);
  image(mainartwork, 0, 0);

  // greetings text
  greetings = loadImage("greetings.png");
  greetings.resize(int(width*.5), 0);
  if (random(1)>0.5) {
    image(greetings, 20, 20);
  } else {
    image(greetings, width/2, height/2-120);
  }

  // white side
  fill(255);
  rect(0, height*.5, width, height*.5);


  stroke(0);
  // mid line
  line(width/2, height/2+ 20, width/2, height-20);

  // stamp placeholder
  rect(width-width/6, height/2+20, width/8, height/8);




  // address
  for (int i =0; i<4; i++) {
    line(width/2+width/12, height-height/4+height/15*i, width-width/12, height-height/4+height/15*i);
  }
  String address_line0 ="To the";
  String address_line1 ="Beehive";
  String address_line2 ="Molesworth St, Pipitea";
  String address_line3 = "Wellington 6011";

  writeFont = createFont("Courier", 32);  
  textFont(writeFont);
  textSize(14);
  fill(0);
  float r = random(3);
  text(address_line0, width/2+width/12, height-height/4+height/15*0-r);
  text(address_line1, width/2+width/12, height-height/4+height/15*1-r);
  text(address_line2, width/2+width/12, height-height/4+height/15*2-r);
  text(address_line3, width/2+width/12, height-height/4+height/15*3-r);

  //the text

  //String thetext = "Dear Ministry for Primary Industries, I noted on your website that there is a process regarding appealing instant fines that have been placed on people for three types of infractions - Bio security, Fishing and Animal Welfare. This includes fee waivers and court hearings. 1.Could you provide the statistics on how many fee waiver requests have been made under each category (Bio security, fishing and animal welfare) within the past 12 months. 2. How many fee waivers have been accepted and how many have been rejected for each category within the past 12 months 3. How many times people have requested a court hearing in each category within the past 12 months. 4.How many court hearings have occurred for each category within the past 12 months Yours faithfully, Ryan S";
  TableRow row = oirs.getRow(int(random(oirs.getRowCount())));
  String thetext = row.getString(0);

  if (thetext.length()<200) {
    textSize(16);
    textLeading(16);
  } else {
    textSize(12);
    textLeading(12);
  }

  int padding = 15;
  text(thetext, padding, height/2+padding*3, width/2-padding*2, height-padding);

  /* String tbc = "To be continued on";
   String theURL = row.getString(1);
   fill(#999999);
   textSize(10);
   text(tbc, padding, height-35);
   textLeading(10);
   text(theURL, padding, height-30, width/2-padding*2, 100);
   */

  // stamp image
  stamp = loadImage("stamps/"+nf(int(random(1, 10)), 2)+".png");
  if (stamp.width>stamp.height) { // landscape
    stamp.resize(120, 0);
    pushMatrix();
    translate(width-width/4, height/2+20);
    rotate(radians(random(-3, 3)));
    image(stamp, 0, 0);
    popMatrix();
  } else { // portrait
    stamp.resize(0, 120);
    pushMatrix();
    translate(width-width/4+20, height/2+20);
    rotate(radians(random(-3, 3)));
    image(stamp, 0, 0);
    popMatrix();
  }

  // post mark
  postmark = loadImage("postmarks/mark_"+nf(int(random(1, 5)), 2)+".png");
  postmark.resize(0, 50);
  pushMatrix();
  translate(width/2+50, height/2+20);
  rotate(radians(random(-3, 3)));
  image(postmark, 0, 0);
  popMatrix();
}
