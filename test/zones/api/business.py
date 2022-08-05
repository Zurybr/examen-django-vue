def delete_spaces(Cadena):
    output_str = ""
    for i in range(len(Cadena)+1):
        if Cadena[i-1:i]!=" ":
            output_str = output_str+Cadena[i-1:i]
        else:    
            if Cadena[i-2:i-1]!=" ":
                output_str = output_str+Cadena[i-1:i]
    return (output_str.strip())