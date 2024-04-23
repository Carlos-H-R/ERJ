#include <GL/glut.h>
#include <math.h>

GLfloat center = 80;
GLfloat frames;

void init();
void frameConter(GLint);
void display();
void reshape(GLint, GLint);
void keyboard(unsigned char, GLint, GLint);

void background();

void sun();
void moon();
void cloud(GLint);

void missile();
void plane();

void character();
void vehicle();

void triangle(GLfloat);
void quad(GLfloat, GLfloat);
void circle(GLint);
void circle_edge(GLint);


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

	background();
	
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
		center -= 0.05;
		if (center < 0) center = 80;
		glutPostRedisplay();
		break;
	
	case 'd':
		center += 0.05;
		if (center >= 80) center = 0;
		glutPostRedisplay();
		break;
	
	default:
		break;
	}
}


// elementos interativos do jogo


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
	glPopMatrix();

	// clouds
	glColor3f(1,1,1);
	glPushMatrix();
		glTranslatef(-8+frames,8,1);
		cloud(0);
	glPopMatrix();
	glPushMatrix();
		glTranslatef(6+frames,7,1);
		cloud(0);
	glPopMatrix();
	
}


// objetos compostos
void sun() {
	glColor4f(0.9922,0.9843,0.8275,);
	circle(30);
}

void moon(GLint phase) {
	glColor4f(0.9609,0.9414,0.832,1);
}

void cloud(GLint type) {
	glColor3f(0.921,0.901,0.847);

	switch (type)
	{
	case 0:
		circle(30);
		break;
	
	default:
		circle(30);
		break;
	}
}


// primitivas
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
