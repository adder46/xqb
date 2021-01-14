document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('close').addEventListener('click', function() {
    this.parentNode.parentNode.parentNode
    .removeChild(this.parentNode.parentNode);
    return false;
  });
});