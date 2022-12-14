# import main Flask class and request object
from flask import Flask, render_template, request
from sympy import *

# create the Flask app
app = Flask(__name__)


@app.route('/')
def template():
    return render_template("index.html")


def midpoint(f, a, b, n):
    error = 1*10**-6
    h = float(b - a)/n  # finding midpoint
    result = 0
    x = a + (h / 2)
    for _ in range(n):
        result += f(x)  # adding all the f(x)
        if(result > error):
            print(error)
        x += h
    result *= h  # multiplying with the midpoint
    return result


def quadraticArea(aq, bq, c, a, b, intervalo):
    x = symbols('x')
    aquadratic = int(aq)
    bquadratic = int(bq)
    cquadratic = int(c)
    f0 = aquadratic*x**2 + bquadratic*x + cquadratic
    f = str(f0)
    raiz1, raiz2 = solve(f)
    area = []
    def f2(x): return eval(f)
    if (a < raiz1 and b <= raiz1):
        rIntegral = integrate(f, (x, a, b))
        area.append(abs(rIntegral))
        aproximacion = midpoint(f2, a, b, intervalo)
        area.append(abs(aproximacion))
    if (a < raiz1 and b > raiz1 and b <= raiz2):
        r1Integral = integrate(f, (x, a, raiz1))
        r2Integral = integrate(f, (x, raiz1, b))
        valueOne = midpoint(f2, a, raiz1, intervalo)
        valueTwo = midpoint(f2, raiz1, b, intervalo)
        aproximacion = abs(valueOne - valueTwo)
        area.append(abs(r1Integral - r2Integral))
        area.append(aproximacion)
    if (a < raiz1 and b > raiz2):
        r1Integral = integrate(f, (x, a, raiz1))
        r2Integral = integrate(f, (x, raiz1, raiz2))
        r3Integral = integrate(f, (x, raiz2, b))
        valueOne = midpoint(f2, a, raiz1, intervalo)
        valueTwo = midpoint(f2, raiz1, raiz2, intervalo)
        valueThree = midpoint(f2, raiz2, b, intervalo)
        aproximacion = abs(valueOne - valueTwo+valueThree)
        area.append(r1Integral - r2Integral + r3Integral)
        area.append(aproximacion)

    if (a >= raiz1 and a < raiz2 and b > raiz1 and b <= raiz2):
        rIntegral = integrate(f, (x, a, b))
        area.append(abs(rIntegral))
        aproximacion = midpoint(f2, a, b, intervalo)
        area.append(abs(aproximacion))
    if (a >= raiz1 and a < raiz2 and b > raiz2):
        r1Integral = integrate(f, (x, a, raiz2))
        r2Integral = integrate(f, (x, raiz2, b))
        area.append(abs(r1Integral - r2Integral))
        valueOne = midpoint(f2, a, raiz2, intervalo)
        valueTwo = midpoint(f2, raiz2, b, intervalo)
        aproximacion = abs(valueOne - valueTwo)
        area.append(aproximacion)
    if (raiz1 == raiz2):
        rIntegral = integrate(f, (x, a, b))
        area.append(abs(rIntegral))
        aproximacion = midpoint(f2, a, b, intervalo)
        area.append(abs(aproximacion))

    area.append(abs(area[0] - area[1]))
    return area


def firstFunction(aExp, nExp, x0, b,intervalo):
    x = symbols('x')
    aExponencial = float(aExp)
    nExponencial = int(nExp)
    f0 = aExponencial*x**nExponencial
    f = str(f0)
    exponente = nExponencial
    area = []
    a = aExponencial

    def f2(x): return eval(f)

    parImpar = ''

    if (exponente % 2 == 0):
        parImpar = "es par"
    else:
        parImpar = "es impar"

    if (parImpar == 'es par' and a > 0 and exponente > 0):
        rIntegral = abs(integrate(f, (x, x0, b)))
        area.append(abs(rIntegral))
        aproximacion = midpoint(f2, x0, b, intervalo)
        area.append(abs(aproximacion))
    if (parImpar == 'es par' and a < 0 and exponente > 0):
        rIntegral = abs(integrate(f, (x, x0, b)))
        area.append(abs(rIntegral))
        aproximacion = midpoint(f2, x0, b, intervalo)
        area.append(abs(aproximacion))
    if (parImpar == 'es impar' and a < 0 and exponente > 0):
        rIntegral = abs(integrate(f, (x, x0, 0)))
        r2Integral = abs(integrate(f, (x, 0, b)))
        area.append(abs(rIntegral - r2Integral))
        valueOne = midpoint(f2, x0, 0, intervalo)
        valueTwo = midpoint(f2, 0, b, intervalo)
        aproximacion = abs(valueOne + valueTwo)
        area.append(aproximacion)
    if (parImpar == 'es impar' and a > 0 and exponente > 0):
        rIntegral = abs(integrate(f, (x, x0, 0)))
        r2Integral = abs(integrate(f, (x, 0, b)))
        area.append(abs(rIntegral - r2Integral))
        valueOne = midpoint(f2, x0, 0, intervalo)
        valueTwo = midpoint(f2, 0, b, intervalo)
        aproximacion = abs(valueOne + valueTwo)
        area.append(aproximacion)
    
    area.append(abs(area[0] - area[1]))

    return area


def sinFunction(aseno, kseno, a, b, intervalo):
    x = symbols('x')
    contadorA = 0
    contadorB = 0
    area = []
    aSenoCasteado = float(eval(aseno))
    k = abs(float(eval(kseno)))
    f = aSenoCasteado*sin(k*x)
    f0 = str(f)
    def f2(x): return eval(f0)
    acasteado = float(eval("a"))
    bcasteado = float(eval("b"))
    picasteado = float(eval("pi"))

    if (a>=0):
        while (contadorA*pi/k <= a):
            contadorA_x_Pi_K = contadorA * pi / k
            if (contadorA_x_Pi_K <= a and a < ((contadorA + 1) * pi / k)):
                if (a < b and b <= ((contadorA + 1) * pi / k)):
                    rIntegral = abs(integrate(f, (x, acasteado, bcasteado)))
                    area.append(rIntegral)
                    aproximacion = abs(midpoint(f2, acasteado, bcasteado, intervalo))
                    area.append(abs(aproximacion))
                else:
                    rIntegral = abs(integrate(f, (x, acasteado, (contadorA + 1) * 
                    picasteado / k)))
                    valueOne = abs(midpoint(f2, acasteado, 
                    (contadorA + 1) * picasteado / k, intervalo))

            contadorA += 1
    else:
        while(contadorA * pi / k >= a):
            contadorA_x_Pi_K = contadorA * pi / k
            if(contadorA_x_Pi_K >= a and a > ((contadorA - 1)* pi / k)):
                if(a < b and b <= ((contadorA) * pi / k)):
                    rIntegral = abs(integrate(f,(x, acasteado, bcasteado)))
                    area.append(rIntegral)
                    aproximacion = abs(midpoint(f2, acasteado, bcasteado, intervalo))
                    area.append(abs(aproximacion))
                else:
                    rIntegral = abs(integrate(f,(x, acasteado, contadorA * 
                    picasteado / k)))
                    # area.append(rIntegral)
                    valueOne = abs(midpoint(f2, acasteado, 
                    contadorA * picasteado / k, intervalo))
            contadorA -= 1
        contadorA = contadorA + 1
        
    contadorB = contadorA

    if (b > contadorB * pi / k):
        while (contadorB * pi / k < b):
            if (contadorB * pi / k < b and b <= ((contadorB + 1) * pi / k)):
                r2Integral = abs(integrate(f, (x, contadorB * picasteado / k,
                 bcasteado)))
                valueTwo = abs(midpoint(f2, contadorB * picasteado / k, bcasteado,
                 intervalo))

            contadorB += 1
        contadorB2 = contadorB - 1
        cant_semiperiodos = contadorB2 - contadorA
        r3Integral = (abs(integrate(f, (x, 0, picasteado / k))) 
        * cant_semiperiodos)
        area.append(rIntegral + r2Integral + r3Integral)
        valueThree = abs(midpoint(f2, 0, picasteado / k, intervalo) 
        * cant_semiperiodos)
        aproximacion = abs(valueOne + valueTwo + valueThree)
        area.append(aproximacion)
    
    area.append(abs(area[0] - area[1]))

    return area


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():

    if request.method == 'POST':
        init_printing()
        x = symbols('x')

        f = request.form.get('f')
        x0 = request.form.get('x0')
        x1 = request.form.get('x1')
        Intervals = request.form.get('intervalos')

        ax = request.form.get('a')
        bx = request.form.get('b')
        c = request.form.get('c')

        aExp = request.form.get('aExponencial')
        nExp = request.form.get('n')

        aseno = request.form.get('aSeno')
        k = request.form.get('k')                  
        typeFunction = request.form.get('function')

        if (typeFunction == 'cuadrática'):
            x = symbols('x')
            intervalsCasteado = int(Intervals)
            x0Casteado = int(x0)
            x1Casteado = int(x1)
            ListIntegralAproximation = quadraticArea(ax, bx, c, x0Casteado, 
            x1Casteado, intervalsCasteado)
            integralDefinida = ListIntegralAproximation[0]
            aproximation = ListIntegralAproximation[1]
            axCasteado = int(ax)
            bxCasteado = int(bx)
            cCasteado = int(c)
            f = axCasteado*x**2 + bxCasteado*x + cCasteado
            integral = integrate(f, x)
            notationScientific = ListIntegralAproximation[2]
            # f2 = lambda x: eval(f)
            # aproximation = midpoint(f2,x0Casteado,x1Casteado,intervalo)
        elif (typeFunction == 'exponencial'):
            x = symbols('x')
            intervalsCasteado = int(Intervals)
            evalx0 = eval(x0)
            evalx1 = eval(x1)
            x0Casteado = float(evalx0)
            x1Casteado = float(evalx1)
            ListIntegralAproximation = firstFunction(aExp, nExp, x0Casteado, 
            x1Casteado, intervalsCasteado)
            integralDefinida = ListIntegralAproximation[0]
            aproximation = ListIntegralAproximation[1]
            aExpCasteado = int(aExp)
            nExpCasteado = int(nExp)
            f = aExpCasteado*x**nExpCasteado
            # f = str(f3)
            # f2 = lambda x: eval(f)
            # aproximation = midpoint(f2,x0Casteado,x1Casteado,10000)
            integral = integrate(f, x)
            notationScientific = ListIntegralAproximation[2]
        elif (typeFunction == 'trigonométrica'):
            x = symbols('x')
            intervalsCasteado = int(Intervals)
            evalx0 = eval(x0)
            evalx1 = eval(x1)
            x0Casteado = float(evalx0)
            x1Casteado = float(evalx1)

            # def f2(x): return eval(f)
            # aproximation = midpoint(f2, x0Casteado, x1Casteado, 10000)
            aSenoCasteado = float(eval(aseno))
            KCasteado = float(eval(k))
            f = aSenoCasteado * sin(KCasteado * x)
            ListIntegralAproximation = sinFunction(aseno, k, evalx0, evalx1, 
            intervalsCasteado)
            integralDefinida = ListIntegralAproximation[0]
            aproximation = ListIntegralAproximation[1]
            integral = integrate(f, x)
            notationScientific = ListIntegralAproximation[2]

        return '''
                <h1>La integral definida de la función elegida (reescrita/simplificada) es: &int;{}</h1>
                <h1>Con sus límites:</h1>
                <ul>
                    <li><h1>Inferior: x<sub>0</sub> = {}</h1></li>
                    <li><h1>Superior: x<sub>1</sub> = {}</h1></li>
                </ul>
                <h1>Solución:</h1>
                <ul>
                    <li><h1>Area bajo la funcion: {}</h1></li>
                    <li><h1>Aproximación: {}</h1></li>
                    <li><h1>Error cometido: {}</h1></li>
                    </ul>
                '''.format(f, x0, x1,integralDefinida, aproximation, 
                notationScientific)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
