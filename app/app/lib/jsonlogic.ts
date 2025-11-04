/**
 * Simple JSONLogic implementation for evaluating conditional display logic
 * Supports the subset of operations needed for questionnaire branching
 */

type JSONLogicData = Record<string, any>;
type JSONLogicRule = any;

/**
 * Evaluate a JSONLogic rule against provided data
 * @param rule - The JSONLogic rule to evaluate
 * @param data - The data context (e.g., {gender: "F"})
 * @returns The result of evaluating the rule
 */
export function evaluateJSONLogic(rule: JSONLogicRule, data: JSONLogicData = {}): any {
  // If rule is a primitive value, return it
  if (rule === null || typeof rule !== 'object' || Array.isArray(rule)) {
    return rule;
  }

  // Get the operator (first key in the rule object)
  const operator = Object.keys(rule)[0];
  const args = rule[operator];

  switch (operator) {
    case 'var': {
      // Get variable from data: {"var": "gender"} -> data.gender
      const path = args;
      return getNestedValue(data, path);
    }

    case '==':
    case '===': {
      // Equality: {"==": [{"var": "gender"}, "F"]}
      if (!Array.isArray(args) || args.length !== 2) return false;
      const left = evaluateJSONLogic(args[0], data);
      const right = evaluateJSONLogic(args[1], data);
      return left === right;
    }

    case '!=':
    case '!==': {
      // Inequality
      if (!Array.isArray(args) || args.length !== 2) return false;
      const left = evaluateJSONLogic(args[0], data);
      const right = evaluateJSONLogic(args[1], data);
      return left !== right;
    }

    case 'in': {
      // Check if value is in array: {"in": [{"var": "gender"}, ["F", "M"]]}
      if (!Array.isArray(args) || args.length !== 2) return false;
      const value = evaluateJSONLogic(args[0], data);
      const array = evaluateJSONLogic(args[1], data);
      return Array.isArray(array) && array.includes(value);
    }

    case 'and': {
      // Logical AND: {"and": [condition1, condition2, ...]}
      if (!Array.isArray(args)) return false;
      return args.every((arg) => evaluateJSONLogic(arg, data));
    }

    case 'or': {
      // Logical OR: {"or": [condition1, condition2, ...]}
      if (!Array.isArray(args)) return false;
      return args.some((arg) => evaluateJSONLogic(arg, data));
    }

    case 'not':
    case '!': {
      // Logical NOT: {"not": condition}
      const value = evaluateJSONLogic(args, data);
      return !value;
    }

    case '>': {
      // Greater than
      if (!Array.isArray(args) || args.length !== 2) return false;
      const left = evaluateJSONLogic(args[0], data);
      const right = evaluateJSONLogic(args[1], data);
      return left > right;
    }

    case '>=': {
      // Greater than or equal
      if (!Array.isArray(args) || args.length !== 2) return false;
      const left = evaluateJSONLogic(args[0], data);
      const right = evaluateJSONLogic(args[1], data);
      return left >= right;
    }

    case '<': {
      // Less than
      if (!Array.isArray(args) || args.length !== 2) return false;
      const left = evaluateJSONLogic(args[0], data);
      const right = evaluateJSONLogic(args[1], data);
      return left < right;
    }

    case '<=': {
      // Less than or equal
      if (!Array.isArray(args) || args.length !== 2) return false;
      const left = evaluateJSONLogic(args[0], data);
      const right = evaluateJSONLogic(args[1], data);
      return left <= right;
    }

    case 'if': {
      // Conditional: {"if": [condition, trueValue, falseValue]}
      if (!Array.isArray(args) || args.length < 2) return null;
      const condition = evaluateJSONLogic(args[0], data);
      if (condition) {
        return evaluateJSONLogic(args[1], data);
      } else if (args.length > 2) {
        return evaluateJSONLogic(args[2], data);
      }
      return null;
    }

    default:
      // Unknown operator - return false for safety
      console.warn(`Unknown JSONLogic operator: ${operator}`);
      return false;
  }
}

/**
 * Get nested value from object by path
 * @param obj - The object to search
 * @param path - The path (e.g., "user.name" or just "name")
 * @returns The value at the path, or undefined if not found
 */
function getNestedValue(obj: any, path: string): any {
  if (!path) return obj;
  
  const keys = path.split('.');
  let current = obj;
  
  for (const key of keys) {
    if (current === null || current === undefined) {
      return undefined;
    }
    current = current[key];
  }
  
  return current;
}

/**
 * Check if a question should be displayed based on its display_if condition
 * @param question - The question with optional display_if condition
 * @param context - The context data (e.g., demographics)
 * @returns true if the question should be shown, false otherwise
 */
export function shouldDisplayQuestion(
  question: { display_if?: any },
  context: JSONLogicData
): boolean {
  if (!question.display_if) {
    // No condition means always display
    return true;
  }
  
  return evaluateJSONLogic(question.display_if, context);
}

/**
 * Check if a question is required based on its required_if condition
 * @param question - The question with required and optional required_if condition
 * @param context - The context data (e.g., demographics)
 * @returns true if the question is required, false otherwise
 */
export function isQuestionRequired(
  question: { required: boolean; required_if?: any },
  context: JSONLogicData
): boolean {
  // If there's a conditional requirement, evaluate it
  if (question.required_if) {
    return evaluateJSONLogic(question.required_if, context);
  }
  
  // Otherwise, use the base required flag
  return question.required;
}

