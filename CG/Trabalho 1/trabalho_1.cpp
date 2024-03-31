#include <GL/glut.h>
#include <math.h>

// só precisa de variável global se o parametro tempo nao for passado para as funções seguintes
GLint frameCounter;

void frameClock(GLint);

void init();
void reshape(GLint, GLint);
void display();

void background();
void keyboard(unsigned char, GLint, GLint);

// primitivas (casa, arvores, nuvens, moinhos, sol, lua)


int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GL_DOUBLE | GL_RGB);

    glutInitWindowPosition(50,50);
    glutInitWindowSize(800,600);

    glutCreateWindow("Trabalho 1");
    init();

    frameClock(frameCounter);
    glutReshapeFunc(reshape);
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);

    glutMainLoop();

    return 0;
}

void frameClock(GLint time) {
    time++;

    glutTimerFunc(10 , frameClock, time);
}

