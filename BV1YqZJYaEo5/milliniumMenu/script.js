document.addEventListener('DOMContentLoaded', () => {
    // DOM元素和状态管理
    const container = document.querySelector('.container');
    const card = document.querySelector('.card');
    const cardInner = document.querySelector('.card-inner');
    const frontOverlay = card.querySelector('.card-front .holographic-overlay');
    let isHovering = false;
    let isFlipped = false;
    let rafId = null;
    let isVisible = false; // 控制卡片是否可见
    
    // 拖动相关状态
    let isDragging = false;
    let startX = 0;
    let startY = 0;
    let currentX = 0;
    let currentY = 0;
    
    // 初始化硬件加速
    card.style.transform = 'translate3d(0,0,0) perspective(1000px)';
    
    // 处理拖动开始
    let dragStartTime = 0;
    let hasMoved = false;
    
    // 修改为监听卡片而不是容器的mousedown事件
    card.addEventListener('mousedown', (e) => {
        if (e.button !== 0) return; // 只响应左键
        
        // 检查点击是否在卡片区域内
        const rect = card.getBoundingClientRect();
        if (e.clientX < rect.left || e.clientX > rect.right || 
            e.clientY < rect.top || e.clientY > rect.bottom) {
            return;
        }
        
        isDragging = true;
        hasMoved = false;
        dragStartTime = Date.now();
        startX = e.clientX - currentX;
        startY = e.clientY - currentY;
        container.style.transition = 'none'; // 拖动时禁用过渡
        e.preventDefault(); // 防止选中文本
    });
    
    // 处理拖动
    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const deltaX = Math.abs(e.clientX - startX - currentX);
        const deltaY = Math.abs(e.clientY - startY - currentY);
        // 如果移动超过3像素，标记为拖动而不是点击
        if (deltaX > 3 || deltaY > 3) {
            hasMoved = true;
        }
        currentX = e.clientX - startX;
        currentY = e.clientY - startY;
        // 更新容器位置，保持transform中的其他属性
        const translateStr = `translate(calc(-50% + ${currentX}px), calc(-50% + ${currentY}px))`;
        container.style.transform = isVisible ? translateStr : `${translateStr} translateY(calc(100vh + 50%))`;
    });
    
    // 处理拖动结束
    document.addEventListener('mouseup', () => {
        isDragging = false;
        container.style.transition = 'transform 0.8s cubic-bezier(0.23, 1, 0.32, 1)';
    });
    
    // 生成3D变换样式
    function updateTransform(rotateX, rotateY, scale = 1, z = 0) {
        return `
            translate3d(0,0,0)
            perspective(1000px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            translateZ(${z}px)
            scale3d(${scale}, ${scale}, ${scale})
        `;
    }
    
    // 处理鼠标移动时的3D效果
    function handleMouseMove(e) {
        if (!isHovering) return;
        
        if (rafId) {
            cancelAnimationFrame(rafId);
        }
        
        const rect = card.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;
        const deltaX = (e.clientX - centerX) * 0.05;
        const deltaY = (e.clientY - centerY) * 0.05;
        
        rafId = requestAnimationFrame(() => {
            // 更新卡片的3D变换
            card.style.transform = updateTransform(-deltaY, deltaX, 1.05, 50);
            
            // 更新正面的全息效果
            const percentX = ((e.clientX - rect.left) / rect.width * 100) + 40;
            const percentY = (e.clientY - rect.top) / rect.height * 100;
            frontOverlay.style.transform = `
                translate(${percentX - 50}%, ${percentY - 50}%)
                rotate(-45deg)
            `;
        });
    }
    
    // 节流函数：限制事件触发频率
    function throttle(func, limit = 16) {
        let inThrottle;
        return function(e) {
            if (!inThrottle) {
                func(e);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        }
    }
    
    // 事件监听器
    // 点击翻转卡片
    card.addEventListener('click', (e) => {
        // 如果是拖动操作，不触发翻转
        if (hasMoved) {
            e.stopPropagation();
            return;
        }
        
        isFlipped = !isFlipped;
        cardInner.classList.toggle('is-flipped');
        
        // 如果当前正在悬浮状态，更新正确面的hover效果
        if (isHovering) {
            // 移除两面的hover效果
            card.querySelector('.card-front').classList.remove('hover');
            card.querySelector('.card-back').classList.remove('hover');
            // 根据翻转状态添加正确面的hover效果
            if (!isFlipped) {
                card.querySelector('.card-front').classList.add('hover');
            } else {
                card.querySelector('.card-back').classList.add('hover');
            }
        }
    });
    
    // 鼠标进入卡片
    card.addEventListener('mouseenter', (e) => {
        isHovering = true;
        card.style.transition = 'transform 0.2s ease-out';
        // 根据当前面添加悬浮效果
        if (!isFlipped) {
            card.querySelector('.card-front').classList.add('hover');
        } else {
            card.querySelector('.card-back').classList.add('hover');
        }
        handleMouseMove(e);
    });
    
    // 鼠标离开卡片
    card.addEventListener('mouseleave', () => {
        isHovering = false;
        if (rafId) {
            cancelAnimationFrame(rafId);
        }
        // 重置所有效果
        card.style.transition = 'transform 0.4s ease-out';
        card.style.transform = updateTransform(0, 0);
        card.querySelector('.card-front').classList.remove('hover');
        card.querySelector('.card-back').classList.remove('hover');
        // 调整重置位置，向右偏移-10%（40%-50%）
        frontOverlay.style.transform = 'translate(-10%, -20%) rotate(-45deg)';
    });
    
    // 添加节流后的鼠标移动监听
    document.addEventListener('mousemove', throttle(handleMouseMove));
    
    // 添加遮罩控制
    let revealCount = 0;
    const maxRevealCount = 5;
    const coveredImage = card.querySelector('.back-image.covered');
    // 定义每次点击后的揭示进度（百分比）
    const revealProgress = [0.3, 0.4, 0.55, 0.7, 1.0];

    function updateRevealMask() {
        // 使用预设的进度值
        const progress = revealProgress[revealCount - 1];
        coveredImage.style.clipPath = `inset(0 0 0 ${progress * 100}%)`; // 从左到右逐渐隐藏遮罩图
    }

    // 监听方向键
    document.addEventListener('keydown', (e) => {
        // 上箭头键显示卡片
        if (e.code === 'ArrowUp' && !isVisible) {
            e.preventDefault();
            isVisible = true;
            container.classList.add('visible');
            // 重置拖动位置
            currentX = 0;
            currentY = 0;
        }
        
        // 右箭头键触发桌面和显示器入场动画，但必须先显示卡片
        if (e.code === 'ArrowRight' && isVisible && !document.querySelector('.desk').classList.contains('slide-in')) {
            e.preventDefault();
            const desk = document.querySelector('.desk');
            const monitor = document.querySelector('.monitor-frame');
            
            // 先显示桌面
            desk.classList.add('slide-in');
            
            // 延迟显示显示器
            setTimeout(() => {
                monitor.classList.add('slide-in');
            }, 250); // 等待桌面动画完成
        }
        
        // 空格键揭示逻辑
        if (e.code === 'Space' && isFlipped && revealCount < maxRevealCount) {
            e.preventDefault();
            if (revealCount === 0) {
                revealCount = 1;
            } else {
                revealCount++;
            }
            updateRevealMask();
        }

        // 回车键自动填充表单
        if (e.code === 'Enter' && loginForm.classList.contains('visible')) {
            e.preventDefault();
            const cardNumberInput = document.getElementById('cardNumber');
            const passwordInput = document.getElementById('password');
            
            // 创建打字机效果
            let cardNumber = "C3L38R0N5-C3NT-M1LL3-AB0NN335";
            let password = "M3RC18CPLAR35ULTAT35TC1-D35U5";
            let cardIndex = 0;
            let passwordIndex = 0;
            
            // 清空输入框
            cardNumberInput.value = '';
            passwordInput.value = '';
            
            // 为卡号创建打字机效果
            const typeCardNumber = setInterval(() => {
                if (cardIndex < cardNumber.length) {
                    cardNumberInput.value += cardNumber[cardIndex];
                    cardIndex++;
                    // 自动滚动到最右边
                    cardNumberInput.scrollLeft = cardNumberInput.scrollWidth;
                } else {
                    clearInterval(typeCardNumber);
                    // 开始输入密码
                    const typePassword = setInterval(() => {
                        if (passwordIndex < password.length) {
                            passwordInput.value += password[passwordIndex];
                            passwordIndex++;
                            // 自动滚动到最右边
                            passwordInput.scrollLeft = passwordInput.scrollWidth;
                        } else {
                            clearInterval(typePassword);
                        }
                    }, 30); // 每个字符之间的延迟
                }
            }, 30); // 每个字符之间的延迟
        }
    });

    // 充值按钮交互
    const menuButtons = document.querySelector('.menu-buttons');
    const loginForm = document.querySelector('.login-form');
    const logo = document.querySelector('.screen-logo');
    const gameCurrency = document.querySelector('.game-currency');
    let hasCardBeenUsed = false; // 添加标记，记录卡是否已被使用
    
    document.querySelectorAll('.menu-btn').forEach((btn, index) => {
        btn.addEventListener('click', (e) => {
            if (btn.textContent === '充值') {
                // 清空表单
                document.getElementById('cardNumber').value = '';
                document.getElementById('password').value = '';
                
                menuButtons.classList.add('hidden');
                logo.classList.add('hidden');
                loginForm.classList.add('visible');
                gameCurrency.classList.add('visible');
            } else if (btn.textContent === '开始') {
                alert('不是，哥们，你还真想玩啊？');
            } else if (btn.textContent === '退出') {
                const shutdownScreen = document.querySelector('.shutdown-screen');
                shutdownScreen.classList.add('visible');
                
                // Windows XP 蓝屏文本
                const shutdownText = [
                    "A problem has been detected and Windows has been shut down to prevent damage",
                    "to your computer.",
                    "",
                    "DRIVER_IRQL_NOT_LESS_OR_EQUAL",
                    "",
                    "If this is the first time you've seen this stop error screen,",
                    "restart your computer. If this screen appears again, follow",
                    "these steps:",
                    "",
                    "Check to make sure any new hardware or software is properly installed.",
                    "If this is a new installation, ask your hardware or software manufacturer",
                    "for any Windows updates you might need.",
                    "",
                    "If problems continue, disable or remove any newly installed hardware",
                    "or software. Disable BIOS memory options such as caching or shadowing.",
                    "If you need to use Safe Mode to remove or disable components, restart",
                    "your computer, press F8 to select Advanced Startup Options, and then",
                    "select Safe Mode."
                ];
                
                let currentLine = 0;
                shutdownScreen.textContent = '';
                
                // 逐行显示文本
                const typeText = () => {
                    if (currentLine < shutdownText.length) {
                        shutdownScreen.textContent += shutdownText[currentLine] + '\n';
                        currentLine++;
                        setTimeout(typeText, 50); // 每行之间的延迟从100ms改为50ms
                    }
                };
                
                typeText();
            }
        });
    });
    
    // 处理取消按钮
    const cancelBtn = loginForm.querySelector('.cancel-btn');
    cancelBtn.addEventListener('click', () => {
        loginForm.classList.remove('visible');
        gameCurrency.classList.remove('visible');
        logo.classList.remove('hidden');
        menuButtons.classList.remove('hidden');
    });
    
    // 处理表单提交
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const cardNumber = document.getElementById('cardNumber').value;
        const password = document.getElementById('password').value;
        
        // 验证卡号和密码，并检查卡是否已使用
        if (cardNumber === "C3L38R0N5-C3NT-M1LL3-AB0NN335" && 
            password === "M3RC18CPLAR35ULTAT35TC1-D35U5" &&
            !hasCardBeenUsed) {
            // 标记卡片已使用
            hasCardBeenUsed = true;
            
            // 更新赛车币数量
            gameCurrency.textContent = "赛车币：200";
            
            // 立即恢复界面
            loginForm.classList.remove('visible');
            gameCurrency.classList.remove('visible');
            // 重置表单状态
            loginForm.style.opacity = '0';
            loginForm.style.pointerEvents = 'none';
            loginForm.style.transform = 'translateY(20px)';
            // 清空表单
            document.getElementById('cardNumber').value = '';
            document.getElementById('password').value = '';
            
            // 显示logo和菜单
            logo.classList.remove('hidden');
            menuButtons.classList.remove('hidden');
            
            // 显示成功提示，独立于界面动画
            const banner = document.querySelector('.notification-banner');
            const text = document.querySelector('.notification-text');
            text.textContent = '恭喜玩家"╰☆壹楗丶仨連ㄋ↖"成功充值200赛车币';
            banner.classList.add('show');
            
            // 3秒后隐藏提示
            setTimeout(() => {
                banner.classList.remove('show');
            }, 3000);
        } else {
            // 显示错误提示
            const banner = document.querySelector('.notification-banner');
            const text = document.querySelector('.notification-text');
            text.textContent = '卡号或密码错误';
            banner.classList.add('show');
            
            // 2秒后隐藏错误提示
            setTimeout(() => {
                banner.classList.remove('show');
            }, 2000);
        }
    });
}); 