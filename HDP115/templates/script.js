
  /*Tabla*/

  function agregarFila() {
    var tablaBody = document.getElementById('tabla-body');
    var nuevaFila = document.createElement('tr');
    
    nuevaFila.innerHTML = '<td contenteditable="true"></td>' +
                          '<td contenteditable="true"></td>' +
                          '<td contenteditable="true"></td>' +
                          '<td contenteditable="true"></td>' +
                          '<td contenteditable="true"></td>' +
                          '<td>' +
                          '  <div class="actions">' +
                          '    <a href="#" onclick="eliminarFila(this)">Eliminar</a>' +
                          '    <a href="#" onclick="editarFila(this)">Editar</a>' +
                          '  </div>' +
                          '</td>';
  
    tablaBody.appendChild(nuevaFila);
  }
  
  function eliminarFila(enlace) {
    var fila = enlace.parentNode.parentNode.parentNode;
    fila.parentNode.removeChild(fila);
  }
  
  function editarFila(enlace) {
    var fila = enlace.parentNode.parentNode.parentNode;
    var celdas = fila.getElementsByTagName('td');
  
    for (var i = 0; i < celdas.length - 1; i++) {
      celdas[i].contentEditable = true;
    }
  }
  