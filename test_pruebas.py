def suma(n, m):
  return n + m

def diferencia_fechas():
  from datetime import datetime

  fecha_inicial = datetime.strptime("01/09/2015 18:20", "%d/%m/%Y %H:%M")
  fecha_final   = datetime.strptime("01/09/2015 19:20", "%d/%m/%Y %H:%M")

  diferencia = fecha_final - fecha_inicial

  segundos_transcurridos = diferencia.total_seconds()
  return segundos_transcurridos

def test_suma():
  assert suma(1, 2) == 3
  assert suma(2, 3) != 6
  assert suma(2, 3) != 10
  
def test_diff_fechas():
  assert diferencia_fechas() == 3600
