def panel_calc(dl_pok, szer_pok, dl_pan, szer_pan, ilosc_pan_w_op):
    pow_pok = (dl_pok*szer_pok)*1.1
    pow_pan = dl_pan*szer_pan
    ilosc_pan = pow_pok/pow_pan

    return round(ilosc_pan/ilosc_pan_w_op)


print("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10)))
