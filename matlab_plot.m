gm = xyceNet{:,"NMN0GM"};
vth = xyceNet{:,"NMN0VTH"};
cgd = -xyceNet{:,"NMN0CGD"};
cgs = -xyceNet{:,"NMN0CGS"};
gds = xyceNet{:,"NMN0GDS"};
id = -xyceNet{:,"IVD"};
vgs = xyceNet{:,"VG"};

vov = vgs-vth;
cgg = cgs + cgd; 
gmro = gm./gds; 
ft = gm./(2*pi*cgg); 
gmid = gm./id; 
ft_gmid = ft.*gmid; 
idw = 1e-6*id; 

subplot(2,3,1)
plot(vgs,id) 
title('V_{gs} vs I_{D}')
xlabel('V_{gs}(V)')
ylabel('I_D{A}')

subplot(2,3,2)
plot(vgs,vov)
title('V_{gs} vs V_{ov}')
xlabel('V_{gs}(V)')
ylabel('V_{ov}{V}')

subplot(2,3,3)
plot(vov,gmid)
title('V_{gs} vs gm/id')
xlabel('V_{ov}(V)')
ylabel('g_m/i_d{V/$\Omega^2$}')

subplot(2,3,4)
plot(gmid,ft)

subplot(2,3,5)
plot(gmid,gmro)

subplot(2,3,6)
plot(gmid,ft_gmid)