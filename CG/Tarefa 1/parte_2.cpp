#include <GL/freeglut_std.h>
#include <GL/freeglut.h>
#include <GL/gl.h>
#include <GL/glut.h>

void square(int x, int y){
    glBegin(GL_POINT);
        glColor3f(1.0,1.0,1.0);
        glPointSize(50);
        glVertex2i(x,y);
    glEnd();
}

void mouse(GLint button, GLint action, GLint x, GLint y){
    switch(button){
        case 1:
            {
                square(x,y);
                break;
            }

        case 2:
            {
                glClearColor(0.0,0.0,0.0,1.0);
            }
    }
}

int main(int argc, char** argv){
    glutInit(&argc,argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize (800, 800);
    glutInitWindowPosition (200, 200);

    glutCreateWindow ("Tarefa 1 - Parte 2");

    glClearColor(0.0,0.0,0.0,1.0);
    glutMouseFunc(mouse);

    glutMainLoop();

    return 0;
}