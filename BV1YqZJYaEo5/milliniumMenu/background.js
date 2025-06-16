document.addEventListener('DOMContentLoaded', () => {
    const background = document.querySelector('.background');
    const loginForm = document.querySelector('.login-form');
    
    // 处理表单提交
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const cardNumber = document.getElementById('cardNumber').value;
        const password = document.getElementById('password').value;
        
        // 这里可以添加验证逻辑
        if (cardNumber && password) {
            // 触发卡片出现的事件
            const event = new CustomEvent('loginSuccess');
            document.dispatchEvent(event);
            
            // 淡出表单
            loginForm.classList.add('fade-out');
        }
    });
}); 