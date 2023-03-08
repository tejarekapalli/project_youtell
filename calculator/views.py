from django.shortcuts import render, redirect, get_object_or_404
from .models import Calculation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def master_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('master_activity_log')
    else:
        form = UserCreationForm()
    return render(request, 'master_signup.html', {'form': form})


def master_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('master_activity_log')
    else:
        form = AuthenticationForm()
    return render(request, 'master_login.html', {'form': form})

@login_required
def master_activity_log(request):
    # Get list of calculations from database
    calculations = []
    
    return render(request, 'master_activity_log.html', {'calculations': calculations})

def master_process_calculation(request, calculation_id):
    # Get calculation from database
    calculation = get_object_or_404(Calculation, id=calculation_id)
    
    # Process calculation and get result
    result = master_process_calculation(calculation)
    
    # Update calculation with result
    calculation.result = result
    calculation.save()
    
    return redirect('master_activity_log')

def student_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_calculate')
    else:
        form = UserCreationForm()
    return render(request, 'student_signup.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_calculate')
    else:
        form = AuthenticationForm()
    return render(request, 'student_login.html', {'form': form})

@login_required
def student_activity_log(request):
    # Get list of calculations from database
    calculations = []
    
    return render(request, 'student_activity_log.html', {'calculation': calculations})

@login_required
def student_calculate(request):
    operands = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    operators = ['plus', 'minus', 'times', 'divided_by']
    
    if request.method == 'POST':
        left_operand = request.POST['left_operand']
        operator = request.POST['operator']
        right_operand = request.POST['right_operand']
        
        calculation = '{}({}({}))'.format(left_operand, operator, right_operand)
        
        # Send calculation to Master for processing
        
        return render(request, 'student_calculate.html', {'operands': operands, 'operators': operators, 'result': result})
    else:
        return render(request, 'student_calculate.html', {'operands': operands, 'operators': operators})



def student_submit_calculation(request):
    if request.method == 'POST':
        left_operand = int(request.POST['left_operand'])
        right_operand = int(request.POST['right_operand'])
        operation = request.POST['operation']
        
        if operation == 'plus':
            result = left_operand + right_operand
        elif operation == 'minus':
            result = left_operand - right_operand
        elif operation == 'times':
            result = left_operand * right_operand
        elif operation == 'divided_by':
            try:
                result = left_operand // right_operand
            except ZeroDivisionError:
                messages.error(request, "Cannot divide by zero")
                return redirect('student_submit_calculation')
        else:
            messages.error(request, "Invalid operation")
            return redirect('student_submit_calculation')
        
        calculation = Calculation.objects.create(
            user=request.user,
            operation=operation,
            left_operand=left_operand,
            right_operand=right_operand,
            result=result
        )
        messages.success(request, "Calculation submitted successfully")
        return redirect('student_activity_log')
    return render(request, 'submit_calculation.html')