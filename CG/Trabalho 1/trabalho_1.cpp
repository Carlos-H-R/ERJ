#include <GL/glut.h>
#include <math.h>

typedef struct Position {
	GLfloat x;
	GLfloat y;
	GLfloat z;
}Position;

GLfloat center = 80;
GLint frames;
Position astro;
Position playerP;


void init();
void frameConter(GLint);
void display();
void reshape(GLint, GLint);
void keyboard(unsigned char, GLint, GLint);

void sky();
void background();

void sun();
void moon();
void cloud(GLint);

void player();
void character();
void vehicle();

void missile();
void plane();

void spaceBox();    // summon vehicle
void heart();       // recover health
void energyCore();  // increase speed for a while

void triangle(GLfloat);
void quad(GLfloat, GLfloat);
void circle(GLint);
void circle_edge(GLint);

void path();


int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

	glutInitWindowSize(800,800);
	glutInitWindowPosition(50,50);

	glutCreateWindow("Trabalho 1");
	init();

	glutDisplayFunc(display);
	glutKeyboardFunc(keyboard);

	glutMainLoop();

	return 0;
}


void init() {
	frames = 0;
	frameConter(frames);

	// player.x

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-10,10,-10,10,1,-1);
}

void frameConter(GLint frame) {
	frames ++;
	glutPostRedisplay();

	glutTimerFunc(10,frameConter,frame);
}

void display() {
	glMatrixMode(GL_MODELVIEW);
	glClearColor(0.5294,0.8078,0.9216,1);

	glClear(GL_COLOR_BUFFER_BIT);

	sky();
	background();

	glPushMatrix();
		character();
	glPopMatrix();
	
	glFlush();
	glutSwapBuffers();
}

void reshape(GLint width, GLint height) {
	// based on width and height 
	// reconfigure exibition of the window
}

void keyboard(unsigned char key, GLint x, GLint y) {
	switch (key)
	{
	case 'a':
		playerP.x -= 0.05;
		center -= 0.05;
		if (center < 0) center = 80;
		glutPostRedisplay();
		break;
	
	case 'A':
		playerP.x -= 0.1;
		center -= 0.1;
		if (center < 0) center = 80;
		glutPostRedisplay();
		break;
	
	case 'd':
		playerP.x += 0.05;
		center += 0.05;
		if (center >= 80) center = 0;
		glutPostRedisplay();
		break;
	
	case 'D':
		playerP.x += 0.1;
		center += 0.1;
		if (center >= 80) center = 0;
		glutPostRedisplay();
		break;
	
	default:
		break;
	}
}


// elementos interativos do jogo


void sky() {
	bool day = (frames % 600) < 300;
	path();

	glPushMatrix();
		glTranslatef(astro.x,astro.y,astro.z);
		sun();
	glPopMatrix();
}

void background() { // subdivide into land, sky and front elements
	// control the background color (day and night cycle based on time)

	glColor3f(0.457,0.6133,0.7421);
	glPushMatrix();
		glTranslatef(-0.25*center,0,0);
		glPushMatrix();
			glTranslatef(-6,-1,0);
			glScalef(10,13,0);
			triangle(1);
		glPopMatrix();
		
		glPushMatrix();
			glTranslatef(0,-1,0);
			glScalef(11,13,0);
			triangle(1);
		glPopMatrix();
		
		glPushMatrix();
			glTranslatef(6,-1,0);
			glScalef(11,15,0);
			triangle(1);
		glPopMatrix();
			
		glPushMatrix();
			glTranslatef(14,-1,0);
			glScalef(10,13,0);
			triangle(1);
		glPopMatrix();
		
		glPushMatrix();
			glTranslatef(20,-1,0);
			glScalef(11,13,0);
			triangle(1);
		glPopMatrix();
		
		glPushMatrix();
			glTranslatef(26,-1,0);
			glScalef(11,15,0);
			triangle(1);
		glPopMatrix();
	glPopMatrix();
	
	glColor3f(0.4863,0.9882,0.0);
	glPushMatrix();
		glTranslatef(-0.5*center,0,0);
		glBegin(GL_POLYGON);
			glVertex3f(-10,-10,0);
			glVertex3f(-10,0,0);
			glVertex3f(10,1,0);
			glVertex3f(20,0.2,0);
			glVertex3f(30,0,0);
			glVertex3f(50,1,0);
			glVertex3f(50,-10,0);
		glEnd();
		// put the background elements here so they enter the loop (between -10 and 50)
		glColor3f(0.07,0.04,0.02);
		glPushMatrix();
			glTranslatef(20,-6.5,0);
			quad(60,3.5);
		glPopMatrix();
	glPopMatrix();

	// clouds (need to include clouds loop)
	glPushMatrix();
		glTranslatef(-8+(frames*0.005),8,1);
		vehicle();
	glPopMatrix();
	glPushMatrix();
		glTranslatef( 6+(frames*0.005),7,1);
		cloud(0);
	glPopMatrix();
	
}


// objetos compostos
void sun() {
	glColor4f(0.9922,0.9843,0.8275,1);
	circle(30);
}

void moon(GLint phase) {
	glColor4f(0.9609,0.9414,0.832,0.5);
	circle(30);
}

void cloud(GLint type) {
	glColor3f(0.921,0.901,0.847);

	switch (type)
	{
	case 0:
		quad(1.5,0.5);
		glPushMatrix();
			glTranslatef(-0.75,0,0);
			glScalef(0.25,0.25,1);
			circle(30);
		glPopMatrix();
		glPushMatrix();
			glTranslatef(0.75,0,0);
			glScalef(0.25,0.25,1);
			circle(30);
		glPopMatrix();
		glPushMatrix();
			glTranslatef(-0.25,0.25,0);
			glScalef(0.5,0.5,1);
			circle(30);
		glPopMatrix();
		glPushMatrix();
			glTranslatef(0.2,0.3,0);
			glScalef(0.5,0.3,1);
			circle(30);
		glPopMatrix();
		break;
	
	default:
		circle(30);
		break;
	}
}


// Game Objects
void character() {
	glColor3f(0.5,0.5,0.5);
	quad(0.1,0.3);
	glPushMatrix();
		glTranslatef(-0.025,-0.4,0);
		quad(0.05,0.5);
	glPopMatrix();
	glPushMatrix();
		glTranslatef(0.025,-0.4,0);
		quad(0.05,0.5);
	glPopMatrix();
	glPushMatrix();
		glTranslatef(0,0.25,0);
		glScalef(0.2,0.2,1);
		circle(30);
	glPopMatrix();
}

void vehicle() {
	glColor3f(0.67,0.67,0.67);
	glPushMatrix();
		glScalef(1.5,0.6,1);
		circle(30);
	glPopMatrix();

	glColor3f(0.7773,0.8867,0.8789);
	glPushMatrix();
		glTranslatef(0,0.5,0);
		glScalef(0.5,0.5,0);
		circle(30);
	glPopMatrix();
}


// Interactive Objects
void spaceBox() {

}

void heart() {

}

void energyCore() {

}


// Primitivas
void triangle(GLfloat side) {
	GLfloat h = (side * sqrt(3)) / 2;
	GLfloat x = side / 2;

	glBegin(GL_TRIANGLES);
		glVertex3f( 0,(2*h)/3, 0);
		glVertex3f( x,-(h/3), 0);
		glVertex3f(-x,-(h/3), 0);
	glEnd();
}

void quad(GLfloat width, GLfloat height) {
	GLfloat w = width / 2;
	GLfloat h = height / 2;

	glBegin(GL_QUADS);
		glVertex3f( w, h, 0);
		glVertex3f( w,-h, 0);
		glVertex3f(-w,-h, 0);
		glVertex3f(-w, h, 0);
	glEnd();
}

void circle(GLint n) {
    glBegin(GL_POLYGON);
        for (int i=0; i<n; i++) {glVertex3f(sin((2*M_PI/n)*i),cos((2*M_PI/n)*i),0);}
    glEnd();
}


void circle_edge(GLint n) {
    glBegin(GL_LINE_LOOP);
        for (int i=0; i<n; i++) {glVertex3f(sin((2*M_PI/n)*i),cos((2*M_PI/n)*i),0);}
    glEnd();
}


void path() {
	GLfloat time = frames % 5000;
	GLfloat fTime = time / 5000;

	// astro.z = 0;
	// astro.x = 0;
	// astro.y = 8.5;

	astro.x = -12 + (24*fTime);
	astro.z =  0;
	astro.y =  8.5 + (-0.1 * pow(astro.x,2));
}
