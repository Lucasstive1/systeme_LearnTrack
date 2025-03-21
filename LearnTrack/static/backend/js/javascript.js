// Fonction pour gérer l'ouverture et la fermeture du sidebar
document.getElementById('sidebarToggle').addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('sidebar-open');
    document.getElementById('contentWrapper').classList.toggle('sidebar-hidden');
});

// Ajouter la fermeture automatique du sidebar au clic externe
document.addEventListener('click', function (e) {
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebarToggle');

    if (!sidebar.contains(e.target) && !sidebarToggle.contains(e.target)) {
        sidebar.classList.remove('sidebar-open');
    }
});

// Initialisation du graphique
const ctx = document.getElementById('performanceChart').getContext('2d');
new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre'],
        datasets: [{
            label: 'Utilisateurs actifs',
            data: [65, 59, 80, 81, 56, 55,],
            borderColor: '#2A5C8B',
            tension: 0.4,
            fill: false
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Performance mensuelle'
            }
        }
    }
});

// Adapter la hauteur du graphique en fonction de la taille de la fenêtre
function resizeChart() {
    const chart = document.getElementById('performanceChart');
    if (window.innerWidth < 768) {
        chart.style.height = '250px';
    } else {
        chart.style.height = '400px';
    }
}

window.addEventListener('resize', resizeChart);
resizeChart();

// Animation au scroll
$(window).on('scroll', function () {
    $('.dashboard-card').each(function () {
        if ($(this).offset().top < $(window).scrollTop() + $(window).height() - 100) {
            $(this).addClass('animate__fadeInUp');
        }
    });
});



// ajout d'un document
 // Compteur de caractères
 const description = document.getElementById('description');
 const charCount = document.getElementById('charCount');
 
 description.addEventListener('input', () => {
     const count = description.value.length;
     charCount.textContent = count;
     if(count > 250) {
         description.classList.add('is-invalid');
         charCount.classList.add('text-danger');
     } else {
         description.classList.remove('is-invalid');
         charCount.classList.remove('text-danger');
     }
 });

 // Affichage du nom de fichier
 const fileInput = document.getElementById('file');
 const fileName = document.getElementById('fileName');
 
 fileInput.addEventListener('change', function(e) {
     if(this.files && this.files.length > 0) {
         fileName.textContent = 'Fichier sélectionné: ' + this.files[0].name;
     }
 });

 // Drag & drop
 const uploadArea = document.querySelector('.upload-area');
 
 uploadArea.addEventListener('dragover', (e) => {
     e.preventDefault();
     uploadArea.style.borderStyle = 'solid';
     uploadArea.style.backgroundColor = 'rgba(52, 152, 219, 0.1)';
 });

 uploadArea.addEventListener('dragleave', () => {
     uploadArea.style.borderStyle = 'dashed';
     uploadArea.style.backgroundColor = '';
 });

 uploadArea.addEventListener('drop', (e) => {
     e.preventDefault();
     fileInput.files = e.dataTransfer.files;
     uploadArea.style.borderStyle = 'dashed';
     uploadArea.style.backgroundColor = '';
     fileName.textContent = 'Fichier sélectionné: ' + e.dataTransfer.files[0].name;
 });