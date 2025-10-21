/**
 * Debugger bypass hook script
 * Overrides the debugger statement functionality to prevent pausing execution
 */

// Override the debugger statement by replacing the Function.prototype.constructor
(function() {
    // Store the original Function constructor
    const originalFunctionConstructor = Function.prototype.constructor;
    
    // Override Function constructor to intercept any attempts to create a function with debugger
    Function.prototype.constructor = function() {
        let args = Array.prototype.slice.call(arguments);
        let body = args[args.length - 1];
        
        // Check if the function body contains debugger statement
        if (typeof body === 'string' && body.includes('debugger')) {
            // Remove or comment out debugger statements
            body = body.replace(/debugger\s*;?/g, '// debugger statement removed');
            args[args.length - 1] = body;
        }
        
        // Call the original constructor with possibly modified arguments
        return originalFunctionConstructor.apply(this, args);
    };
    
    // Make the override non-configurable so it can't be easily reverted
    Object.defineProperty(Function.prototype, 'constructor', {
        configurable: false,
        writable: false,
        enumerable: false,
        value: Function.prototype.constructor
    });
})();

// Alternative approach: Override eval function as well since it can also contain debugger statements
(function() {
    const originalEval = window.eval;
    
    window.eval = function(code) {
        if (typeof code === 'string') {
            // Remove debugger statements from evaluated code
            code = code.replace(/debugger\s*;?/g, '// debugger statement removed');
        }
        return originalEval.call(this, code);
    };
    
    // Make the override non-configurable
    Object.defineProperty(window, 'eval', {
        configurable: false,
        writable: false,
        enumerable: false,
        value: window.eval
    });
})();

// Override the global debugger statement itself (this is a no-op but makes the statement ineffective)
window.debugger = function() {
    // Intentionally empty - overrides any attempts to call debugger as a function
};

console.log('[+] Debugger bypass hook loaded successfully');