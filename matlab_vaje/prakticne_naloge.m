GRAFI = 0;

% naloga 1 - place ------------------------------------------------
place = [1157 1151 1158 1170 1146 1152 1149 1155 1148	1168	1147	1169;
1106 1098 1080 1095	1094 1112 1097 1112	1105 1098 1106 1106;
596	572	586	585	589	600	581	591	582	572	591	603;
912	933	941	916	909	927	919	938	923	929	913	918;
786	770	780	776	780	781	787	776	789	774	778	784;
1138 1135 1151 1145	1124 1164 1136 1156	1156 1142 1143 1159;
902	893	919	913	891	904	893	899	911	888	904	912;
958	977	967	964	955	972	966	964	975	956	961	961];

% letni prejemki
o11 = sum(place, 2);
% izdatki po mesecih
o12 = sum(place, 1);
% povprecni mesecni zasluzek
o13 = mean(mean(place));
% povprecni letni zasluzek
o14 = mean(o11);

if GRAFI
    % histogram po mesecih
    meseci = 1:12;
    vrednosti = [mean(place); min(place); max(place)];
    figure(0101);
    bar(meseci, vrednosti);
    
    % histogram letnega prihodka po osebah
    figure(0102);
    bar([o11]);
end

% naloga 2 - prostornina piramide ------------------------------------------------
A = [0,1,0];
B = [2,1,2];
C = [3,1,1];
D = [-2,2,3];

% vektorji robov piramide 
a = B - A;
b = C - A;
c = D - A;

triple_product = dot(a, cross(b,c));
o21 = abs(triple_product) / 6;

% naloga 3 - studij ------------------------------------------------
studentje = load("studentje.csv");

% povprecna razlika po spolu
dekleta = studentje(studentje(:,2)==1, :);
fantje = studentje(studentje(:,2)==0, :);
o31 = mean(dekleta(:,3) - fantje(:,3));

if GRAFI
    % histogram stevila po letih
    figure(0301);
    bar([fantje(:,3)'; dekleta(:,3)']');
end

% najvec studentov in studentk
o32 = fantje(find(fantje(:,3) == max(fantje(:,3))), 1);
o33 = dekleta(find(dekleta(:,3) == max(dekleta(:,3))), 1);

% naloga 4 - casovna zahtevnost ------------------------------------------------
f1 = @(x) x .* log(x) + 15./x;
f2 = @(x) x .^3 ./ 4 + 3 .* x;

if GRAFI
    figure(0401);
    X = linspace(0, 20, 1000);
    hold on
    plot(X, f1(X));
    plot(X, f2(X));
    legend("prvi", "drugi");
    hold off
end

% za katere n je prvi vecji
X = 1:20;
vrednosti = [f1(X);f2(X)];
o41 = find(vrednosti(1,:) > vrednosti(2,:));

% naloga 5 - place II ------------------------------------------------

place2 = place;
place2(:,1) = place(:,1) * 5/4;
place2(:,2) = place(:,2) - ( place(:,4) + place(:,5) ) / 10;
place2(:,12) = place(:,12) + (sum(place(:, 1:11), 2) / 15) + 500;

% povprecna placa po mesecu 
po_mesec = mean(place2);
% povprecja po tromesecjih 
s = movmean(po_mesec,3);
o51 = s(2:3:end);

% naloga 6 - polinom ------------------------------------------------

% TODO

% naloga 7 - place II ------------------------------------------------

