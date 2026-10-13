import data as D
H={h["id"]:h for h in D.HORMONAS}
E={c:v for g,c,v,n in D.ELEGIBILIDAD}
MIDX={"cu":0,"lng":1,"imp":2,"ampd":3,"psp":4,"ahc":5}
def cat(cond,m): return E[cond][MIDX[m]]
def ctx(items,tipo,eid):
    out=[]
    for x in items:
        if x.startswith("Las "): continue
        if ":" in x[:28]:
            p,rest=x.split(":",1); p=p.strip().lower(); rest=rest.strip()
            ok = (p=="sola" and tipo in("psp","dng_solo")) or (p in("combinada","combinado") and tipo=="ahc") or (p.startswith("con valerato") and eid=="e2") or (p.startswith("con etinilestradiol") and eid=="ee")
            if ok: out.append(rest[0].upper()+rest[1:])
            continue
        out.append(x)
    return out
def ficha(g):
    nombre,pid,pd,eid,ed,tipo,marcas=g
    P=H.get(pid); ES=H.get(eid)
    f={"grupo":nombre,"marcas":[m.strip() for m in marcas.split(",")],"tipo":tipo}
    if tipo=="thm":
        f["tipoTxt"]="Terapia hormonal (menopausia o ginecológica), no anticonceptivo"
        f["sirve"]=["Tratamiento de síntomas de la menopausia o indicaciones ginecológicas específicas. No se usa para evitar embarazo."]
        f["peso"]="—"; f["tromb"]="Los estrógenos orales en terapia hormonal también aumentan el riesgo de trombosis; se evalúa caso a caso."
        f["cv"]=["Requiere evaluación médica: hipertensión, antecedentes de trombosis o de cáncer hormono-dependiente."]
        f["cancer"]=["Terapia hormonal combinada prolongada: leve aumento de cáncer de mama; se indica la dosis y el tiempo mínimos."]
        f["noUsar"]=["Embarazo","Cáncer de mama o de endometrio","Trombosis activa o previa","Sangrado genital sin estudiar"]
        f["nota"]="Aparece en la tabla de equivalencias, pero se usa como terapia hormonal y no como anticonceptivo. Revisa la indicación en el envase."
        return f
    if tipo=="pae":
        f["tipoTxt"]="Anticoncepción de emergencia"
        f["sirve"]=["Evitar el embarazo después de una relación sin protección o si falló el método. Retrasa la ovulación; no es abortiva.","Mayor eficacia mientras antes se tome, hasta 72 horas (algo de efecto hasta 120 h)."]
        f["peso"]="No afecta el peso."; f["tromb"]="Sin aumento demostrado."
        f["cv"]=["La OMS la considera segura incluso con hipertensión, migraña o antecedentes cardiovasculares (categoría 1–2)."]
        f["cancer"]=["Sin relación conocida con cáncer."]
        f["noUsar"]=["No sirve como método habitual (menos eficaz que un método regular)","Embarazo confirmado (no tiene efecto)"]
        f["nota"]="Con IMC 30 o más puede ser menos eficaz. Iniciar un método regular después."
        return f
    m = "ahc" if tipo=="ahc" else "psp"
    f["tipoTxt"]={"ahc":"Anticonceptivo combinado oral (estrógeno + progestina)","psp":"Píldora de progestágeno solo","dng_solo":"Progestina sola (tratamiento de endometriosis)"}[tipo]
    sirve=["Evitar el embarazo: 7 de cada 100 mujeres se embarazan al año con uso típico y 0,3 con uso perfecto."] if tipo!="dng_solo" else ["Tratamiento del dolor por endometriosis. Suele inhibir la ovulación, pero no está registrado como anticonceptivo: usar otro método para evitar embarazo."]
    sirve+=ctx(P["beneficios"],tipo,eid)
    if tipo=="ahc": sirve+=["Ciclos regulares y menos dolor menstrual","Protege contra cáncer de endometrio y de ovario con el uso prolongado"]
    f["sirve"]=sirve
    f["peso"]="Puede disminuir la hinchazón por su efecto antimineralocorticoide; no engorda." if pid=="drsp" else "Los estudios no muestran aumento de peso atribuible a la píldora."
    f["tromb"]=P["vte"] if tipo=="ahc" else "Sin aumento claro del riesgo de trombosis."
    if tipo=="ahc" and eid=="ee" and ed in ("0,02 mg","0,015 mg"): f["tromb"]+=" Dosis baja de etinilestradiol; el riesgo depende sobre todo de la progestina."
    if tipo=="ahc":
        f["cv"]=[f"Hipertensión controlada: categoría {cat('Hipertensión controlada',m)}; presión 160/100 o más: categoría {cat('Presión 160/100 mmHg o más',m)} (no usar).",
                 f"Fuma y tiene 35 años o más: categoría {cat('Fuma, 35 años o más, menos de 15 cigarrillos al día',m)} (menos de 15 cigarrillos) o {cat('Fuma, 35 años o más, 15 o más cigarrillos al día',m)} (15 o más).",
                 f"Migraña con aura: categoría {cat('Migraña con aura',m)} (no usar). Migraña sin aura: categoría {cat('Migraña sin aura',m)}.",
                 f"Antecedente de trombosis o trombofilia: categoría 3 a 4."]
        f["cancer"]=["Mama: pequeño aumento mientras se usa (RR 1,2–1,3); categoría 4 si hay cáncer de mama actual.",
                     "Cuello uterino: leve aumento con 5 años o más de uso; mantener PAP al día.",
                     "Endometrio y ovario: disminuye el riesgo, y la protección dura décadas."]
    else:
        f["cv"]=[f"Hipertensión, incluso 160/100 o más: categoría {cat('Hipertensión controlada','psp')}–{cat('Presión 160/100 mmHg o más','psp')} (se puede usar).",
                 f"Fumadora de 35 años o más: categoría {cat('Fuma, 35 años o más, 15 o más cigarrillos al día','psp')}.",
                 f"Migraña con aura: categoría {cat('Migraña con aura','psp')}. Alternativa cuando el estrógeno está contraindicado."]
        f["cancer"]=["Mama: pequeño aumento similar al de los combinados (RR 1,2–1,3); categoría 4 si hay cáncer de mama actual."]
    no=ctx(P["noUsar"],tipo,eid)
    if tipo=="ahc":
        no=[x for x in (ES["noUsar"] if ES and ES["id"]=="ee" else D.HORMONAS[0]["noUsar"])]+ctx(P["noUsar"],tipo,eid)
    f["noUsar"]=list(dict.fromkeys(no))
    if tipo=="dng_solo":
        f["sirve"]=[x for x in f["sirve"] if "acné" not in x]
        f["noUsar"]=["Embarazo","Cáncer de mama actual","Sangrado genital sin estudiar","Enfermedad hepática grave"]
        f["cv"]=["Sin estrógeno: se puede considerar con hipertensión o migraña, con control médico."]
    f["nota"]={"cpa":"Indicado sobre todo para acné o hirsutismo; no se recomienda solo como anticonceptivo.",
               "dsg":"La píldora de 0,075 mg sirve en lactancia; margen de olvido de 12 horas." if tipo=="psp" else "",
               "nomac":"Usa estradiol idéntico al natural; esquema 24+4.",}.get(pid,"")
    f["prog"]=P["nombre"]; f["estr"]=ES["nombre"] if ES else "Sin estrógeno"
    return f
FICHAS=[ficha(g) for g in D.EQUIV]
if __name__=="__main__":
    import json; print(json.dumps(FICHAS[5],ensure_ascii=False,indent=1)[:2500])
