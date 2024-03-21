#include <GL/glut.h>
#include <stdio.h>
#include <math.h>


void display();

void quadrado(GLfloat x, GLfloat y, GLfloat z, GLfloat size);
void retangulo(GLfloat x, GLfloat y, GLfloat z, GLfloat height, GLfloat width);
void triangulo(GLfloat x, GLfloat y, GLfloat z, GLfloat height, GLfloat base);
void circulo(GLint n);
void circunferencia(GLint n);
void helice();
void roda();

void carro();
void background();
void moinho();
void sol();

int main(int argc, char** argv){
    glutInit(&argc,argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize (800, 800);
    glutInitWindowPosition (200, 200);

    glutCreateWindow ("Tarefa 1 - Parte 1");

    // Estado Inicial
    glClearColor(1.0,1.0,1.0,1.0);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-10,10,-10,10,-1,1);

    // desenho
    display();

    glutMainLoop();

    return 0;
}


void display(){
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_LINES);
        glColor3f(0,0,0);
        glVertex3f(-10,0,0);
        glVertex3f(10,0,0);
        glVertex3f(0,-10,0);
        glVertex3f(0,10,0);
    glEnd();

    sol();

    glFlush();
}


void quadrado(GLfloat x, GLfloat y, GLfloat z, GLfloat size){
    float s = size/2;
    
    glBegin(GL_QUADS);
        glVertex3f(x-s,y+s,z);
        glVertex3f(x+s,y+s,z);
        glVertex3f(x+s,y-s,z);
        glVertex3f(x-s,y-s,z);
    glEnd();
}


void retangulo(GLfloat x, GLfloat y, GLfloat z, GLfloat height, GLfloat width){
    float h = height/2;
    float w = width/2;
    
    glBegin(GL_QUADS);
        glVertex3f(x-w,y+h,z);
        glVertex3f(x+w,y+h,z);
        glVertex3f(x+w,y-h,z);
        glVertex3f(x-w,y-h,z);
    glEnd();
}


void triangulo(GLfloat x, GLfloat y, GLfloat z, GLfloat height, GLfloat base){
    float b = base/2;

    glBegin(GL_TRIANGLES);
        glVertex3f(x-b,y,z);
        glVertex3f(x,y+height,z);
        glVertex3f(x+b,y,z);
    glEnd();
}


void helice(){
    glColor3f(0.8,0.3,0.3);

    glBegin(GL_POLYGON);
        glVertex3f(0,0,0);
        glVertex3f(0.25,0.1,0);
        glVertex3f(1,0,0);
        glVertex3f(0.25,-0.1,0);
    glEnd();
}


void circulo(GLint n){
    glBegin(GL_POLYGON);
        for (int i=0; i<n; i++) {glVertex3f(sin((2*3.1415/n)*i),cos((2*3.1415/n)*i),0);}
    glEnd();
}


void circunferencia(GLint n){
    glBegin(GL_LINE_LOOP);
        for (int i=0; i<n; i++) {glVertex3f(sin((2*3.1415/n)*i),cos((2*3.1415/n)*i),0);}
    glEnd();
}


void roda(){
    glColor3f(0.5,0.5,0.5);

    circulo(100);

    glColor3f(0,0,0);
    glBegin(GL_LINES);
        for (int i=0; i<12; i++) {
            glVertex3f(0,0,0);
            glVertex3f(sin((2*3.1415/12)*i),cos((2*3.1415/12)*i),0);
        }
    glEnd();

    glLineWidth(5);
    circunferencia(100);
}


void carro(){
    glPushMatrix();
    glTranslatef(0.75,-0.3,0);
    glScalef(0.3,0.3,1);
    roda();
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-0.75,-0.3,0);
    glScalef(0.3,0.3,1);
    roda();
    glPopMatrix();
    

    glColor3f(1,0,0);
    retangulo(0,0.5,0,1,3);
    retangulo(-0.4,1.25,0,0.5,1);
}


void moinho(){
    glColor3f(0.4,0.4,0.4);
    retangulo(0,0.5,0,1,0.1);

    glPushMatrix();
    glTranslatef(0,1,0);
    glScalef(0.5,0.8,1);
    helice();
    glPushMatrix();
    glRotated(120,0,0,1);
    helice();
    glPushMatrix();
    glRotated(120,0,0,1);
    helice();
    glPopMatrix();
    glPopMatrix();
    glPopMatrix();
}


void sol(){
    glColor3f(1,1,0.5);

    glColor3f(1,0.75,0);
    glBegin(GL_LINES);
        for (int i=0; i<12; i++) {
            glVertex3f(0,0,0);
            glVertex3f(1.3*sin((2*3.1415/12)*i),1.3*cos((2*3.1415/12)*i),0);
        }
    glEnd();

    circulo(100);

    glLineWidth(5);
    circunferencia(100);
}


void background(){
    glColor3f(0,1,0);
    // glBegin(GL_POLYGON);
    //     glVertex3f(-10,,0);
    //     glVertex3f(-10,,0);
    //     glVertex3f(,,0);
    //     glVertex3f(,,0);
    //     glVertex3f(,,0);
    //     glVertex3f(,,0);
    //     glVertex3f(,,0);
    //     glVertex3f(,,0);
    //     glVertex3f(,,0);
}
