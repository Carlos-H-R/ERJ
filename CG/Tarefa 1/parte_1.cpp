#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include <GL/freeglut.h>

void house(int x, int y){
    glBegin(GL_QUADS);
        glColor3f(0.0,1.0,0.0);
        glVertex2i(x,y);
        glVertex2i(x+100,y+100);
    glEnd();

    glBegin(GL_TRIANGLES);
        glColor3f(1.0,0.0,0.0);
        glVertex2i(x,y);
        glVertex2i(x+50,y+50);
        glVertex2i(x+100,y);
    glEnd();

}

void keyboard(unsigned char key, GLint x, GLint y){
    if (key == 32){
        glClearColor(1.0,1.0,1.0,1.0);
    }
    
    else{
        glClearColor(0.0,0.0,0.0,1.0);
    }
}

int main(int argc, char** argv){
    glutInit(&argc,argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize (800, 800);
    glutInitWindowPosition (200, 200);

    glutCreateWindow ("Tarefa 1 - Parte 1");

    house(50,50);
    glutKeyboardFunc(keyboard);

    glutMainLoop();

    return 0;
}