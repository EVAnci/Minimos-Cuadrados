#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>

// Función para calcular los coeficientes a y b del ajuste lineal y = ax + b
void linear_fit(const std::vector<double>& x, const std::vector<double>& y, double& a, double& b) {
    double n = x.size();
    double sum_x = std::accumulate(x.begin(), x.end(), 0.0);
    double sum_y = std::accumulate(y.begin(), y.end(), 0.0);
    double sum_xx = std::inner_product(x.begin(), x.end(), x.begin(), 0.0);
    double sum_xy = std::inner_product(x.begin(), x.end(), y.begin(), 0.0);
    
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x);
    b = (sum_y - a * sum_x) / n;
}

// Función para calcular el error cuadrático medio
double mean_squared_error(const std::vector<double>& x, const std::vector<double>& y, double a, double b) {
    double mse = 0.0;
    for (size_t i = 0; i < x.size(); ++i) {
        double y_pred = a * x[i] + b;
        mse += (y[i] - y_pred) * y[i] - y_pred;
    }
    return mse / x.size();
}

int main() {
    // Datos experimentales
    std::vector<double> t = {1, 2, 3, 4, 5};
    std::vector<double> i = {8.187, 6.703, 5.488, 4.493, 3.679};
    
    // Transformación logarítmica
    std::vector<double> ln_i(i.size());
    std::transform(i.begin(), i.end(), ln_i.begin(), [](double val) { return std::log(val); });
    
    // Ajuste lineal
    double a, b;
    linear_fit(t, ln_i, a, b);
    
    // Cálculo de las constantes
    double RC = -1.0 / a;
    double i_0 = std::exp(b);
    
    // Cálculo del error
    double mse = mean_squared_error(t, ln_i, a, b);
    
    // Resultados
    std::cout << "RC: " << RC << std::endl;
    std::cout << "i_0: " << i_0 << std::endl;
    std::cout << "Mean Squared Error: " << mse << std::endl;
    
    return 0;
}
