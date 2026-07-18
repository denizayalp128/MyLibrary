const searchInput = document.getElementById('search');
    const bookList = document.getElementById('book-list');

    searchInput.addEventListener('input', () => {
      const query = searchInput.value.trim().toLowerCase();
      const rows = bookList.querySelectorAll('tr');
      let hasVisible = false;

      rows.forEach(row => {
        const cells = Array.from(row.querySelectorAll('td'));
        const text = cells.map(cell => cell.textContent.toLowerCase()).join(' ');
        const visible = query === '' || text.includes(query);
        row.style.display = visible ? '' : 'none';
        if (visible) {
          hasVisible = true;
        }
      });

      const emptyRow = bookList.querySelector('.empty-row');
      if (emptyRow) {
        emptyRow.style.display = hasVisible ? 'none' : '';
      }
    });