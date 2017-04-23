clear all
close all

time = [0.25077680212 1.75823438215 13.0119599093 141.123480073 1571.18099093 17790.6549749]
samples = [1e2 1e3 1e4 1e5 1e6 1e7]



k=0.001;

figure(1)


scatter(samples, time,'Linewidth',4)
set(gca,'xscale','log')
hold on
plot(samples, k*(2*samples+1),'Linewidth',4)


str = ['Teórica: F(V,E) = ',num2str((k)),' * (V+E)'];



xgca = gca;
xgca.FontSize = 20;
title('Elementos fuertemente conexos')
grid on
xlabel('Muestras')
ylabel('Tiempo [mS]')
legend('Mensurada',str)

