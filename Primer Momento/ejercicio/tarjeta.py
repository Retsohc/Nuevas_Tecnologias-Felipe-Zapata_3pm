
def tarjeta_credito():
    valor_tarjeta = float(input("Ingresa el valor de la tarjeta de crédito: "))
    
    saldo_tarjeta = valor_tarjeta
    cuotas = 5
    
    while saldo_tarjeta > 0:
        
        opcion = input("¿Deseas hacer una compra? (1. Sí / 2. No): ")
        
        if opcion == '2':
            print("Gracias, vuelva pronto.")
            break
        
        if opcion != '1':
            print("Opción no válida. Introduce 1 para continuar o 2 para finalizar.")
            continue
        
        valor_compra = float(input("Ingresa el valor de la compra: ")) 
        print("")
         
        if valor_compra > saldo_tarjeta:
            print("La compra excede el valor de la tarjeta.")
            continue
        
        deuda_inicial = valor_compra
        valor_cuota = deuda_inicial / cuotas
        total_pagado = 0
        
        for i in range(cuotas):
            total_pagar = valor_cuota
            saldo_tarjeta -= valor_cuota
            total_pagado += total_pagar
            
            print(f"Cuota {i+1}: Pagaste {total_pagar:.2f} (Cuota: {valor_cuota:.2f}), Saldo restante de la tarjeta: {saldo_tarjeta:.2f}")
            
            if saldo_tarjeta <= 0:
                break
        
        print("\nPago completo. Deuda totalmente pagada.")
        print(f"Saldo restante de la tarjeta: {saldo_tarjeta:.2f}\n")
        







