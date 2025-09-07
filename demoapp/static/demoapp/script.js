// Script para la barra lateral
document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggleSidebar');
    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('sidebar-collapsed');
        sidebar.classList.toggle('sidebar-visible');
    });

    // script para la selección de nombres
    const info = {
        claro: {
            empresa: 'Claro',
            codigo: 'CL001',
            descripcion: 'Empresa líder en telecomunicaciones en Latinoamérica.'
        },
        movistar: {
            empresa: 'Movistar',
            codigo: 'MV002',
            descripcion: 'Proveedor global de servicios de telefonía y datos.'
        },
        tigo: {
            empresa: 'Tigo',
            codigo: 'TG003',
            descripcion: 'Operador de telecomunicaciones con presencia internacional.'
        }
    };
    const select = document.getElementById('nombre');
    const infoDiv = document.getElementById('info-nombre');
    select.addEventListener('change', function() {
        const value = select.value;
        if (info[value]) {
            infoDiv.innerHTML = `
                <h5>${info[value].empresa}</h5>
                <p><strong>Código:</strong> ${info[value].codigo}</p>
                <p>${info[value].descripcion}</p>
            `;
        } else {
            infoDiv.innerHTML = '<span class="text-muted">Selecciona un nombre para ver la información.</span>';
        }
    });
});